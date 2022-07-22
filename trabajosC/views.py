import datetime as dtime
from django.core.files.storage import FileSystemStorage 
from django.http import JsonResponse
import json
from django.db.models import Q
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Paragraph, Frame

from django.views import View

from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from django.shortcuts import  redirect, render
from Cursos.forms import EspecialidadesForm
from trabajosC.forms import AutoresForm2, AutoresForm3, InstitucionForm, ManuscritosForm, TablasForm, Trabajo_AutoresForm, TrabajosCForm

from trabajosC.models import Autores, Cursos, Especialidades, Instituciones, Manuscritos, Tablas, Trabajos, Trabajos_has_autores

# Create your views here.

def index(request):
    if request.user.is_superuser:
        trabajos = Trabajos.objects.all()
        autores = Autores.objects.all()
        cursos = Cursos.objects.filter(user= request.user.id)
        
        autores_trab = Trabajos_has_autores.objects.all()
        manuscritos = Manuscritos.objects.all().select_related('trabajo')
        
        return render(request,'admin.html', {'autores':autores,'trabajos':trabajos,'cursos':cursos,'manuscritos':manuscritos,'autores_trab':autores_trab, 'formEspecialidad' : EspecialidadesForm()})
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
                    data['error'] = 'No es posible registrar el trabajo, ha exedido la fecha limite'
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
                    trab.palabras_claves = trabj['palabras_claves']
                    trab.resumen_ingles = trabj['resumen_ingles']
                    trab.keywords = trabj['keywords']
                    trab.curso_id = trabj['curso']
                    
                    trab.save()
                    otros_autores = trabj['otros_autores']

                    for i in otros_autores:
                        if len(i) != 0:
                            a = int(i)
                            aut = Autores.objects.get(id = a)
                            Trabajos_has_autores.objects.create(trabajo_id=trab.id, autor_id =aut.id)
                        #m1.save() 
                                       
                    for file in manuscritos:
                        fs = FileSystemStorage(location=manus_path, base_url=manus_path)
                        name1 = fs.save(trab.Autor_correspondencia.Nombres+trab.titulo+file.name,file)
                        obj = Manuscritos(
                            tituloM = trab.Autor_correspondencia.Nombres+trab.titulo+file.name,
                            manuscrito = '/manuscritos/'+name1,
                            trabajo = trab
                            )
                        obj.save(force_insert=True )

                    for file in tablas:
                        fs = FileSystemStorage(location=manus_path2, base_url=manus_path2)
                        name1 = fs.save(trab.Autor_correspondencia.Nombres+trab.titulo+file.name,file)
                        obj = Tablas(
                            tituloM = trab.Autor_correspondencia.Nombres+trab.titulo+file.name,
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
        context['manuscritosForm'] = ManuscritosForm()
        context['tablasForm'] = TablasForm()
        context['trabajo_autorForm'] = Trabajo_AutoresForm()
        context['action'] = 'add'
        

        return context


class TrabajosPDF(View):

    def get(self, request, *args, **kwargs):

        trabajo = Trabajos.objects.get(pk=self.kwargs['pk'])
        autores_trab = Trabajos_has_autores.objects.filter(trabajo_id=self.kwargs['pk'])
        manuscritos = Manuscritos.objects.filter(trabajo_id=self.kwargs['pk'])
        styleSheet = getSampleStyleSheet()
        style = styleSheet['BodyText']
        P=Paragraph('This is a very silly example',style)
        #create Canvas
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
        
        aW = 60    # available width and height
        aH = 200
        w,h = P.wrap(aW, aH)    # find required space
        if w<=aW and h<=aH:
            P.drawOn(p,0,aH)
            aH = aH - h         # reduce the available height
            p.setTitle(trabajo.titulo)
            p.setFont("Helvetica-Bold", 20)
            p.drawCentredString(300, 50, trabajo.titulo)
            p.line(50, 100,550,100)
            #Create a text object
            textob = p.beginText()        
            textob.setTextOrigin(1.2*inch, 2*inch)
            textob.setFont("Helvetica", 14)
            #agregar Lineas 
            Lines = []
            #Lines.append(trabajo.titulo)
            Lines.append("Observaciones: ")
            Lines.append(trabajo.observaciones)
            Lines.append("Resumen en español: ")
            Lines.append(trabajo.resumen_esp)
            Lines.append("Palabras claves: ")
            Lines.append(trabajo.palabras_claves)
            Lines.append("Resumen en ingles: ")
            Lines.append(trabajo.resumen_ingles)
            Lines.append("Keywords: ")
            Lines.append(trabajo.keywords)

            #bucles
            for line in Lines:
                textob.textLine(line)
            #Finish up
            p.drawText(textob)
            # Close the PDF object cleanly, and we're done.
            p.showPage()
            p.save()
            buffer.seek(0)
        else:
            raise ValueError
        
        return FileResponse(buffer, as_attachment=True, filename='example.pdf')

        """ pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size= 16)
        pdf.cell(200, 10, txt = "Trial to generate a pdf file.", ln=2, align='C')
        pdf.output('media/pdf/Attempt.pdf','F') """
