import datetime as dtime
import os
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import json
from django.db.models import Q
from django.core.files.storage import default_storage,FileSystemStorage
from django.core.files.base import ContentFile
from django.urls import reverse, reverse_lazy
from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView,DetailView,UpdateView
from django.views.decorators.clickjacking import xframe_options_exempt
from django.shortcuts import  redirect, render

from Cursos.forms import EspecialidadesForm
from trabajosC.forms import AutoresForm2, AutoresForm3, EvaluadorTrabajoForm, InstitucionForm, KeywordForm, ManuscritosForm, Palabras_clavesForm, TablasForm, Trabajo_AutoresForm, Trabajo_InstitucionesForm, Trabajo_KeywordsForm, Trabajo_PalabrasForm, TrabajosCForm
from trabajosC.funciones.funciones2 import email_confirmTC, handle_uploaded_file

from trabajosC.models import Autores, Cursos, Especialidades, Instituciones, Keywords, Manuscritos, Palabras_claves, Tablas, Trabajos, Trabajos_has_Keywords, Trabajos_has_autores, Trabajos_has_instituciones, Trabajos_has_palabras

from trabajosC.funciones.funciones1 import convert_to_pdf_wd ,generate_pdf_linux

# Create your views here.
@xframe_options_exempt
def index(request):
    """ 
    Index del proyecto. 

    **Context**    

        ``trabajos``:  Una instancia modelo del Trabajos creado en la app trabajosC`.
            
        ``autores``: Una instancia modelo del Autores creado en la app trabajosC`.
        
        ``cursos``: Una instancia del modelo Cursos creado en la app trabajosC`.
        
        ``autores_trab``: Una instancia del modelo Trabajos_has_autores creado en la app trabajosC`.
        
        ``palabras_trab``: Una instancia del modelo Trabajos_has_palabras creado en la app trabajosC`.
        
        ``manuscritos``: Una instancia del modelo Manuscritos creado en la app trabajosC`.

    **Returns**

        1. Vista de aministrador con la lista de las instancias.
        2. Vista del formulario de registro de trabajo si no es administrador.
    """
    #Validación si el usuario logeado es superuser(Admin)
    if request.user.is_authenticated:
        if request.user.is_superuser:
            trabajos = Trabajos.objects.all().only("identificador","tipo_trabajo", "subtipo_trabajo","titulo","Autor_correspondencia", "institucion_principal","curso")
            autores = Autores.objects.all().defer( "especialidad","direccion")
            cursos = Cursos.objects.all()
            
            autores_trab = Trabajos_has_autores.objects.all()
            palabras_trab = Trabajos_has_palabras.objects.all()

            manuscritos = Manuscritos.objects.all().select_related('trabajo')
            
            return render(request,'admin.html', {'autores':autores,'trabajos':trabajos,'cursos':cursos,'manuscritos':manuscritos,'autores_trab':autores_trab,'palab_trab':palabras_trab, 'formEspecialidad' : EspecialidadesForm()})
        else:
            return redirect('misEvaluaciones')
    else:
        return redirect('create_Trabajo')

def is_ajax(request):
    ''' Función para Validar que el metodo enviado desde javascript sea ajax '''
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def ajax_especialidades(request):
    '''  Esta función recibe un request ajax para registrar especialidades desde el formulario de registro de autores.
    **Return** 
        1. Retorna la especialidad creada en formato Json para ser mostrada en el campo de especialidad del  formulario de registro de autores.
        2. Retorna un mensaje de error si ya existía la especialidad o de exito al ser creada.
    '''
    if is_ajax(request=request):
        data ={}
        if request.method == 'GET':
            especialidad = request.GET.get('especialidad')
            with transaction.atomic():
                especialidades = Especialidades.objects.filter(Q(especialidad__icontains=especialidad))
                if especialidades:
                    data['error'] = 'No es posible registrar la especialidad, ya existe'
                else:
                    instance = Especialidades.objects.create(especialidad=especialidad)
                    data = instance.toJSON()
                    data['mensaje'] = 'Especialidad creada con exito!'

                return JsonResponse(data,safe=False)
        else:                
            return JsonResponse(data)
       

class registrarTrabajo(CreateView):
    ''' Clase CreateView para registrar los trabajos científicos. 

    **Context**  

        :Trabajos:  Una instancia del modelo Trabajos creado en la app trabajosC.

    **Methods**

        :``post(self, request, *args, **kwargs)``: 

            Recibe todas las peticiones post enviadas por AJAX desde el formulario de registro de trabajos.

        :``get_context_data(self, **kwargs)``: 

            Envio del context al formulario de registrar trabajos.

    **Template:**

        :template_name: Formulario para la creación del trabajo científico.
    '''
    model = Trabajos
    form_class= TrabajosCForm
    template_name='createTrabajo.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        '''Recibe todas las peticiones post enviadas por AJAX desde el formulario de registro de trabajos.'''
        data = {}
        manus_path = 'media/manuscritos'
        manus_path2 = 'media/otros'

        try:
            action = request.POST['action']
            if action == 'search_autor':
                data = []
                term = request.POST['term']
                autores = Autores.objects.filter(
                    Q(Nombres__icontains=term) | Q(Apellidos__icontains=term))[0:10]
                for i in autores:
                    item = i.toJSON()
                    item['text'] = i.get_full_name()
                    data.append(item)
                    
            elif action == 'search_curso':
                term = request.POST['curso_id']
                curso = Cursos.objects.get(id=term)
                if curso.fecha_fin < dtime.date.today():
                    data['error'] = 'No es posible registrar el trabajo, ha excedido la fecha límite'
                    return JsonResponse(data, safe=False)
               
            elif action == 'search_institucion':
                data = []
                term = request.POST['term']
                instituciones = Instituciones.objects.filter(
                    Q(institucion__icontains=term))[0:10]
                for i in instituciones:
                    item = i.toJSON()
                    item['text'] = i.institucion
                    data.append(item)
            
            elif action == 'search_palabrasClaves':
                data = []
                term = request.POST['term']
                palabras = Palabras_claves.objects.filter(
                    Q(palabra__icontains=term))[0:10]
                for i in palabras:
                    item = i.toJSON()
                    item['text'] = i.palabra
                    data.append(item)
            
            elif action == 'agregar_palabras_claves':
                with transaction.atomic():
                    frmplb = Palabras_clavesForm(request.POST)                    
                    data = frmplb.save()
            
            elif action == 'search_keywords':
                data = []
                term = request.POST['term']
                keywords = Keywords.objects.filter(
                    Q(keyword__icontains=term))[0:10]
                for i in keywords:
                    item = i.toJSON()
                    item['text'] = i.keyword
                    data.append(item)
            
            elif action == 'agregar_keywords':
                with transaction.atomic():
                    frmkey = KeywordForm(request.POST)                    
                    data = frmkey.save()
            
            elif action == 'create_autor1':
                with transaction.atomic():
                    frmAutor = AutoresForm2(request.POST)
                    data = frmAutor.save()

            elif action == 'create_autor2':
                with transaction.atomic():
                    frmAutor = AutoresForm2(request.POST)
                    data = frmAutor.save()

            elif action == 'create_institucion':
                with transaction.atomic():
                    frmInst = InstitucionForm(request.POST)                    
                    data = frmInst.save()

            elif action == 'add':
                with transaction.atomic():
                    cont=0
                    autores = []
                    trabj = json.loads(request.POST['trabajo'])
                    manuscritos = request.FILES.getlist('manuscritos')
                    tablas = request.FILES.getlist('tablas')

                    trab = Trabajos()
                    trab.tipo_trabajo = trabj['tipo_trabajo']
                    trab.subtipo_trabajo = trabj['subTipo_trabajo']
                    trab.titulo = trabj['titulo']
                    trab.Autor_correspondencia_id = trabj['Autor_correspondencia']
                    trab.observaciones = trabj['observaciones']
                    trab.institucion_principal_id = trabj['institucion_principal']
                    trab.resumen_esp = trabj['resumen_esp']
                    trab.resumen_ingles = trabj['resumen_ingles']
                    
                    trab.curso_id = trabj['curso']                    
                    trab.save()
                    otros_autores = trabj['otros_autores']
                    otras_inst = trabj['otras_instituciones']

                    palabras_claves = trabj['palabras_claves']
                    keywords = trabj['keywords']

                    for i in palabras_claves:
                        if len(i) != 0:
                            a = int(i)
                            pal = Palabras_claves.objects.get(id = a)
                            Trabajos_has_palabras.objects.create(trabajo_id=trab.id, palabra_id =pal.id)
                           
                    for i in keywords:
                        if len(i) != 0:
                            a = int(i)
                            key = Keywords.objects.get(id = a)
                            Trabajos_has_Keywords.objects.create(trabajo_id=trab.id, keyword_id =key.id)

                    for i in otros_autores:
                        if len(i) != 0:
                            a = int(i)
                            aut = Autores.objects.get(id = a)
                            Trabajos_has_autores.objects.create(trabajo_id=trab.id, autor_id =aut.id)

                    for i in otras_inst:
                        if len(i) != 0:
                            a = int(i)
                            inst = Instituciones.objects.get(id = a)
                            Trabajos_has_instituciones.objects.create(trabajo_id=trab.id, institucion_id =inst.id)

                    for file in manuscritos:
                        fs = FileSystemStorage(location=manus_path, base_url=manus_path)
                        postfix=os.path.splitext(file.name)[1][1:]
                        nombre_curso = trab.curso.nombre_curso
                        if "Libre" in trab.tipo_trabajo or "Ingreso" in trab.tipo_trabajo:
                            cant_trabajos= Trabajos.objects.filter(curso_id = trab.curso_id).filter(Q(tipo_trabajo__icontains="Libre") | Q(tipo_trabajo__icontains="Ingreso")).count()
                            if "Libre" in trab.tipo_trabajo:
                                name1 = fs.save(nombre_curso+'/'+"LI"+str(cant_trabajos)+'.'+postfix,file)
                                obj = Manuscritos(
                                tituloM = "LI"+str(cant_trabajos)+'.'+postfix,
                                manuscrito = '/manuscritos/'+name1,
                                trabajo = trab
                                )
                                trab.identificador = 'LI'+str(cant_trabajos)
                            else:
                                name1 = fs.save(nombre_curso+'/'+"IN"+str(cant_trabajos)+'.'+postfix,file)
                                obj = Manuscritos(
                                tituloM = "IN"+str(cant_trabajos)+'.'+postfix,
                                manuscrito = '/manuscritos/'+name1,
                                trabajo = trab
                                )
                                trab.identificador = 'IN'+str(cant_trabajos)

                        elif "E-poster" in trab.tipo_trabajo:
                            cant_trabajos= Trabajos.objects.filter(curso_id = trab.curso_id).filter(tipo_trabajo__icontains="E-poster").count()
                            name1 = fs.save(nombre_curso+'/'+"EP"+str(cant_trabajos)+'.'+postfix,file)
                            obj = Manuscritos(
                            tituloM = "EP"+str(cant_trabajos)+'.'+postfix,
                            manuscrito = '/manuscritos/'+name1,
                            trabajo = trab
                            )
                            trab.identificador = 'EP'+str(cant_trabajos)
                            
                        trab.save()
                        obj.save(force_insert=True )

                    for file in tablas:
                        postfix=os.path.splitext(file.name)[1][1:]
                        fs = FileSystemStorage(location=manus_path2, base_url=manus_path2)
                        name1 = fs.save(nombre_curso+'/'+"anexo"+trab.tipo_trabajo+str(cant_trabajos)+'.'+postfix,file)
                        obj = Tablas(
                            tituloT = "anexo"+trab.tipo_trabajo+str(cant_trabajos)+'.'+postfix,
                            tabla = '/otros/'+name1,
                            trabajo = trab
                            )
                        obj.save(force_insert=True )
                    AutorP = Autores.objects.get(id = trab.Autor_correspondencia_id)
                    nombre = AutorP.get_full_name()
                    correo = AutorP.email
                    n_curso = trab.curso
                    email_confirmTC(nombre, correo, trab.titulo,n_curso)
                    messages.success(request, 'Trabajo cargado con exito!')

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        '''Envio del context(forms, tiles, etc) al formulario registro de trabajos.'''        
        context = {}
        context['title'] = 'Registrar Trabajo'
        context['form'] = self.form_class
        context['form2'] = AutoresForm2()
        context['form3'] = AutoresForm3()
        context['form4'] = InstitucionForm()
        context['form5'] = Palabras_clavesForm()
        context['form6'] = KeywordForm()

        context['manuscritosForm'] = ManuscritosForm()
        context['tablasForm'] = TablasForm()
        context['trabajo_autorForm'] = Trabajo_AutoresForm()
        context['trabajo_instiForm'] = Trabajo_InstitucionesForm()
        context['trabajo_instiForm'] = Trabajo_InstitucionesForm()
        context['trabajo_palbForm'] = Trabajo_PalabrasForm()
        context['trabajo_keywForm'] = Trabajo_KeywordsForm()
        #context['search_form'] = SearchForm()
        context['action'] = 'add'
        

        return context

class TrabajoDetailView(DetailView):
    """Clase DetailView para ver la información del trabajo científico.

    **Context**    

        ``trabajos``:  Una instancia modelo del Trabajos creado en la app trabajosC`.

    **Template:**

        :template_name: Template para ver la información del trabajo científico.
    """
    model = Trabajos
    template_name='trabajoInfo.html'

    def get_queryset(self):
        qs = super(TrabajoDetailView, self).get_queryset()
        return qs.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manuscritos'] = Manuscritos.objects.filter(trabajo_id=self.kwargs['pk'])
        context['anexos'] = Tablas.objects.filter(trabajo_id=self.kwargs['pk'])        
        return context
 
class AsignarEvaluadorTC(UpdateView):
    ''' Clase UpdateView para actualizar el evaluador del trabajo científico. 

    **Context** 
       
        :model:  Una instancia del modelo Trabajos creado en la app trabajosC.
        :form_class:  Formulario para la edición del evaluador creado en forms.py de la app Trabajos.
        :success_url:  Al ser exitoso la actualización del evaluador redirecciona al index.
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al formulario de editar evaluador.

        :``post(self, request,pk, *args, **kwargs)``: 

            Metodo que recibe la información del evaluador seleccionado en el formulario para hacer las respectivas validaciones.

    **Template:**

        :template_name: Formulario para la edición del evaluador.
            
    '''
    model = Trabajos
    form_class = EvaluadorTrabajoForm
    template_name = 'evaluador.html'
    success_url = reverse_lazy('inicio')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        manus_path = 'media/manuscritos/'
        out_folder = 'media/manuscritos'
        contador=0
        form = self.form_class(request.POST, instance=self.object)
        Trabajo = self.object
        manuscritos = Manuscritos.objects.filter(trabajo = Trabajo)
        for i in manuscritos:
            manuscrito1 =i
            break
        file_name = os.path.splitext(manuscrito1.tituloM)[0]
        postfix=os.path.splitext(manuscrito1.tituloM)[1][1:]
        otros_autores = Trabajos_has_autores.objects.filter(trabajo_id = Trabajo.id)

        if form.is_valid():
            #print(request.POST.getlist('confirmacion'))
            if form.cleaned_data['evaluador'] == None:
                messages.warning(request, 'No ha seleccionado a ningun Evaluador')
                return redirect('inicio')
            elif not request.POST.getlist('confirmacion'):
                messages.warning(request, 'No ha confirmado la revision del manuscrito')
                return redirect('inicio')
            else:
                for obj in otros_autores:
                    if obj.autor == form.cleaned_data['evaluador']:
                        contador +=1          
                if contador ==0 and Trabajo.Autor_correspondencia != form.cleaned_data['evaluador'] and (postfix=='docx' or postfix=='doc'):
                    convert_to_pdf_wd(manus_path+manuscrito1.tituloM, out_folder)
                    #generate_pdf_linux(manus_path+manuscrito1.tituloM, out_folder,timeout=15) 
                    ruta_pdf = 'manuscritos/'+file_name+".pdf"
                    consultaM = Manuscritos.objects.filter(tituloM = file_name+'.pdf')
                    if not consultaM:                        
                        obj = Manuscritos(
                            tituloM = file_name+'.pdf',
                            manuscrito = ruta_pdf,
                            trabajo = Trabajo
                            )
                        obj.save(force_insert=True )
                    form.save()
                    messages.success(request, 'Evaluador asignado con exito')
                elif postfix=='pptx':
                    form.save()
                    messages.success(request, 'Evaluador asignado con exito')
                else:
                    messages.error(request, 'No se puede asignar evaluador, hace parte del trabajo')
                return redirect('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Asignar Evaluador'
        context['entity'] = 'TrabajosCientificos'
        
        return context

class ManuscritoEdit(UpdateView):
    """Clase UpdateView para actualizar el manuscrito del trabajo científico.

    **Context**  

        :model:  Una instancia del modelo Manuscritos creado en la app trabajosC.
        :form_class:  Formulario para la edición del manuscrito creado en forms.py de la app Trabajos.
        :success_url:  Al ser exitoso la actualización del manuscrito redirecciona al index.

    **Methods**

        :``post(self, request, *args, **kwargs)``: 

            Recibe el documento actualizado y valida si tiene el mismo nombre para poder actualizar la bd.

        :``get_context_data(self, **kwargs)``: 

            Envio del context al formulario de editar manuscrito.
    """
    model = Manuscritos
    form_class = ManuscritosForm
    template_name = 'manus_editModal.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance= self.object)        
        trabajo_id = self.object.trabajo_id
        trb = Trabajos.objects.get(id = trabajo_id)
        curso = Cursos.objects.get(id = trb.curso_id)
        manus_path = 'manuscritos/'+str(curso.nombre_curso)+'/'
        doc = request.FILES['manuscrito']
        if form.is_valid():
            if self.object.tituloM == doc.name:
                default_storage.delete(manus_path+self.object.tituloM)
                handle_uploaded_file(manus_path,doc)
                manus =Manuscritos.objects.get(id=self.object.id)
                manus.tituloM = doc.name
                manus.manuscrito = manus_path+doc.name
                manus.save()
            else:
                messages.error(request, 'El documento no tiene el mismo nombre que el subido por el autor!')
            return redirect('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Editar Manuscrito'
        context['manus'] = Manuscritos.objects.all()        
        return context


