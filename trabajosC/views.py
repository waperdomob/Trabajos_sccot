import datetime as dtime
import traceback
from django.contrib import messages

from django.core.files.storage import FileSystemStorage 
from datetime import datetime
from django.http import JsonResponse
import json
from django.db.models import Q

from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView,ListView, UpdateView,DeleteView,DetailView

from django.shortcuts import  redirect, render
from numpy import save
from trabajosC.forms import AutoresForm, AutoresForm2, AutoresForm3, ManuscritosForm, TablasForm, Trabajo_AutoresForm, Trabajo_InstitucionesForm, TrabajosCForm

from trabajosC.models import Autores, Cursos, Instituciones, Manuscritos, Tablas, Trabajos, Trabajos_has_autores, Trabajos_has_instituciones

# Create your views here.

def index(request):
    if request.user.is_superuser:
        trabajos = Trabajos.objects.all()
        manuscritos = Manuscritos.objects.all().select_related('trabajo')
        
        return render(request,'admin.html', {'trabajos':trabajos,'manuscritos':manuscritos})
    else:
        return render(request,'index.html')

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
        manus_path2 = 'media/tablas'

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
                    
            if action == 'search_curso':
                term = request.POST['curso_id']
                curso = Cursos.objects.get(id=term)
                if curso.fecha_fin < dtime.date.today():
                    data['error'] = 'No es posible registrar el trabajo, ha exedido la fecha limite'
                    return JsonResponse(data, safe=False)
               
            elif action == 'create_autor1':
                with transaction.atomic():
                    frmAutor = AutoresForm2(request.POST)
                    data = frmAutor.save()

            elif action == 'create_autor2':
                with transaction.atomic():
                    frmAutor = AutoresForm2(request.POST)
                    data = frmAutor.save()
            
            elif action == 'add':
                    cont=0
                    autores = []
                    trabj = json.loads(request.POST['trabajo'])
                    manuscritos = request.FILES.getlist('manuscritos')
                    tablas = request.FILES.getlist('tablas')

                    trab = Trabajos()
                    trab.tipo_trabajo = trabj['tipo_trabajo']
                    trab.titulo = trabj['titulo']
                    trab.Autor_correspondencia_id = trabj['Autor_correspondencia']
                    trab.observaciones = trabj['observaciones']
                    trab.institucion_principal = trabj['institucion_principal']
                    trab.resumen_esp = trabj['resumen_esp']
                    trab.palabras_claves = trabj['palabras_claves']
                    trab.resumen_ingles = trabj['resumen_ingles']
                    trab.keywords = trabj['keywords']
                    trab.curso_id = trabj['curso']
                    trab.save()

                    otras_instituciones = trabj['otras_instituciones']
                    otros_autores = trabj['otros_autores']

                    for i in otros_autores:
                        a = int(i)
                        aut = Autores.objects.get(id = a)

                        Trabajos_has_autores.objects.create(trabajo_id=trab.id, autor_id =aut.id)
                        print("save")
                        #m1.save()

                    for i in otras_instituciones:
                        a = int(i)
                        inst = Instituciones.objects.get(id = a)
                        m2 = Trabajos_has_instituciones.objects.create(trabajo_id=trab.id, institucion_id=inst.id)
                        m2.save()   
                                       
                    for file in manuscritos:
                        fs = FileSystemStorage(location=manus_path, base_url=manus_path)
                        name1 = fs.save(trab.Autor_correspondencia.Nombres+trab.titulo+file.name,file)
                        obj = Manuscritos(
                            tituloM = trab.Autor_correspondencia.Nombres+trab.titulo+file.name,
                            manuscrito = '/manuscritos/'+name1,
                            trabajo = trab
                            )
                        obj.save(force_insert=True )
                        print("save")
                    for file in tablas:
                        fs = FileSystemStorage(location=manus_path2, base_url=manus_path2)
                        name1 = fs.save(trab.Autor_correspondencia.Nombres+trab.titulo+file.name,file)
                        obj = Tablas(
                            tituloM = trab.Autor_correspondencia.Nombres+trab.titulo+file.name,
                            tabla = '/tablas/'+name1,
                            trabajo = trab
                            )
                        obj.save(force_insert=True )
                        print("save")
                    

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):        
        context = {}
        context['title'] = 'Registrar Trabajo'
        context['form'] = self.form_class
        context['form2'] = AutoresForm2()
        context['form3'] = AutoresForm3()
        context['manuscritosForm'] = ManuscritosForm()
        context['tablasForm'] = TablasForm()
        context['trabajo_autorForm'] = Trabajo_AutoresForm()
        context['trabajo_instituForm'] = Trabajo_InstitucionesForm()


        context['action'] = 'add'

        return context


class registrarAutor(CreateView):
    model = Autores
    form_class= TrabajosCForm
    template_name='createTrabajo.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_autor':
                data = [{'id': '', 'text': '------------'}]
                for i in Autores.objects.filter(id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.Nombres})
            elif action == 'search_autores':
                data = [{'id': '', 'text': '------------'}]
                for i in Autores.objects.filter(id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.Nombres})
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):        
        context = {}
        context['title'] = 'Registrar Trabajo'
        context['form'] = self.form_class
        context['form2'] = AutoresForm()

        return context

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.get_context_data())

def create_autor(request):

    return redirect('create_Trabajo')