import datetime as dtime
import os
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import json
from django.db.models import Q
import io
from django.core.files.storage import default_storage,FileSystemStorage
from docx2pdf import convert
import pythoncom
from django.urls import reverse, reverse_lazy
from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView,DetailView,UpdateView
from django.shortcuts import  redirect, render

from django.views import View
from Cursos.forms import EspecialidadesForm
from trabajosC.forms import AutoresForm2, AutoresForm3, EvaluadorTrabajoForm, InstitucionForm, KeywordForm, ManuscritosForm, Palabras_clavesForm, TablasForm, Trabajo_AutoresForm, Trabajo_InstitucionesForm, Trabajo_KeywordsForm, Trabajo_PalabrasForm, TrabajosCForm

from trabajosC.models import Autores, Cursos, Especialidades, Instituciones, Keywords, Manuscritos, Palabras_claves, Tablas, Trabajos, Trabajos_has_Keywords, Trabajos_has_autores, Trabajos_has_instituciones, Trabajos_has_palabras

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            trabajos = Trabajos.objects.all().only("id","tipo_trabajo", "subtipo_trabajo","titulo","Autor_correspondencia", "institucion_principal","curso")
            autores = Autores.objects.all().defer( "especialidad","direccion")
            cursos = Cursos.objects.filter(user= request.user.id)
            
            autores_trab = Trabajos_has_autores.objects.all()
            palabras_trab = Trabajos_has_palabras.objects.all()

            manuscritos = Manuscritos.objects.all().select_related('trabajo')
            
            return render(request,'admin.html', {'autores':autores,'trabajos':trabajos,'cursos':cursos,'manuscritos':manuscritos,'autores_trab':autores_trab,'palab_trab':palabras_trab, 'formEspecialidad' : EspecialidadesForm()})
        else:
            return redirect('misEvaluaciones')
    else:
        return redirect('create_Trabajo')

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def ajax_especialidades(request):
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
    model = Trabajos
    form_class= TrabajosCForm
    template_name='createTrabajo.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
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
                        #m1.save() 
                    for i in otras_inst:
                        if len(i) != 0:
                            a = int(i)
                            inst = Instituciones.objects.get(id = a)
                            Trabajos_has_instituciones.objects.create(trabajo_id=trab.id, institucion_id =inst.id)
                        #m1.save() 
                    for file in manuscritos:
                        fs = FileSystemStorage(location=manus_path, base_url=manus_path)
                        postfix=os.path.splitext(file.name)[1][1:]
                        name1 = fs.save(trab.tipo_trabajo+str(trab.id)+'.'+postfix,file)
                        obj = Manuscritos(
                            tituloM = trab.tipo_trabajo+str(trab.id)+'.'+postfix,
                            manuscrito = '/manuscritos/'+name1,
                            trabajo = trab
                            )
                        obj.save(force_insert=True )

                    for file in tablas:
                        postfix=os.path.splitext(file.name)[1][1:]
                        fs = FileSystemStorage(location=manus_path2, base_url=manus_path2)
                        name1 = fs.save(trab.tipo_trabajo+str(trab.id)+'.'+postfix,file)
                        obj = Tablas(
                            tituloM = trab.tipo_trabajo+str(trab.id)+'.'+postfix,
                            tabla = '/otros/'+name1,
                            trabajo = trab
                            )
                        obj.save(force_insert=True )


        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):        
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

    model = Trabajos
    template_name='trabajoInfo.html'

    def get_queryset(self):
        qs = super(TrabajoDetailView, self).get_queryset()
        return qs.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manuscritos'] = Manuscritos.objects.filter(trabajo_id=self.kwargs['pk'])
                
        return context
 
class AsignarEvaluadorTC(UpdateView):
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
        pythoncom.CoInitialize()
        form = self.form_class(request.POST, instance=self.object)
        Trabajo = self.object
        manuscritos = Manuscritos.objects.filter(trabajo = Trabajo)
        for i in manuscritos:
            manuscrito1 =i
            break
        file_name = os.path.splitext(manuscrito1.tituloM)[0]
        otros_autores = Trabajos_has_autores.objects.filter(trabajo_id = Trabajo.id)

        if form.is_valid():
            if form.cleaned_data['evaluador'] == None:
                messages.warning(request, 'No ha seleccionado a ningun Evaluador')
                return redirect('inicio')
            else:
                for obj in otros_autores:
                    if obj.autor == form.cleaned_data['evaluador']:
                        contador +=1
                    else:
                        contador=0            
                if contador ==0 and Trabajo.Autor_correspondencia != form.cleaned_data['evaluador']:
                    messages.success(request, 'Evaluador asignado con exito')
                    convert(manus_path+manuscrito1.tituloM)
                    ruta_pdf = 'manuscritos/'+file_name+".pdf"
                    consultaM = Manuscritos.objects.get(tituloM = file_name+'.pdf')
                    if not consultaM:                        
                        obj = Manuscritos(
                            tituloM = file_name+'.pdf',
                            manuscrito = ruta_pdf,
                            trabajo = Trabajo
                            )
                        obj.save(force_insert=True )
                    form.save()
                else:
                    messages.error(request, 'No se puede asignar evaluador, hace parte del trabajo')
                return redirect('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Asignar Evaluador'
        context['entity'] = 'TrabajosCientificos'
        
        return context

class ManuscritoEdit(UpdateView):
    model = Manuscritos
    form_class = ManuscritosForm
    template_name = 'manus_editModal.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        manus_path = 'manuscritos/'
        pythoncom.CoInitialize()
        form = self.form_class(request.POST, request.FILES, instance= self.object)        
        trabajo_id = self.object.trabajo_id
        doc = request.FILES['manuscrito']
        if form.is_valid():
            if self.object.tituloM == doc.name:
                default_storage.delete(manus_path+self.object.tituloM)
                form.save()
            else:
                messages.error(request, 'El documento no tiene el mismo nombre que el subido por el autor!')
            return redirect('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Editar Manuscrito'
        context['manus'] = Manuscritos.objects.all()        
        return context


