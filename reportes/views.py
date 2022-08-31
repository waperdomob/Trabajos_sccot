from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.views.generic import TemplateView
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.db.models import FloatField, F

from reportes.forms import reportForm
from reportes.funciones.funciones import filtrar
from trabajosC.models import Autores, Cursos, Especialidades, Instituciones, Trabajos, Trabajos_has_autores
from usuario.mixins import IsSuperuserMixin

# Create your views here.
class reporteTC(IsSuperuserMixin,TemplateView):
    template_name= 'reporte.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
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
                data = []
                term = request.POST['term']
                cursos = Cursos.objects.filter(Q(nombre_curso__icontains=term))[0:10]
                for i in cursos:
                    item = i.toJSON()
                    item['text'] = i.nombre_curso
                    data.append(item)

            elif action == 'search_inst':
                data = []
                term = request.POST['term']
                instituciones = Instituciones.objects.filter(Q(institucion__icontains=term))[0:10]
                for i in instituciones:
                    item = i.toJSON()
                    item['text'] = i.institucion
                    data.append(item)

            elif action == 'search_report':
                data = []
                j=0
                autor = request.POST.get('autor','')
                curso = request.POST.get('curso','')
                institucion = request.POST.get('institucion','')
                tipoT = request.POST.get('tipoTrabajo','')
                trabajos = filtrar(curso,autor,institucion, tipoT)
                autores_trab = Trabajos_has_autores.objects.all().prefetch_related('trabajo')
                autores=[]
                for object in trabajos:
                    aut_tb = []
                    for autor in autores_trab:                        
                        if autor.trabajo_id == object.id :
                            aut_tb.append(autor.autor.get_full_name())
                    autores.append(aut_tb)
                for i in trabajos:
                    data.append([
                        i.identificador,
                        i.curso.nombre_curso,
                        i.titulo,
                        i.tipo_trabajo,
                        i.subtipo_trabajo,
                        i.Autor_correspondencia.get_full_name(),
                        i.Autor_correspondencia.email,
                        autores[j],
                        i.institucion_principal.institucion,
                        i.Autor_correspondencia.ciudad,
                        i.fecha_subida.strftime('%Y-%m-%d'),
                        i.curso.fecha_fin.strftime('%Y-%m-%d'),
                        format(i.calificacion),
                    ])
                    j+=1
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte Trabajos Científicos'
        context['list_url'] = reverse_lazy('reportes')
        context['form'] = reportForm()
        context['action'] = 'search_report'
        return context  