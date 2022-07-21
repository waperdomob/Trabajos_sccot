import datetime as dtime
from django.http import JsonResponse
from django.db.models import Q

from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView,DeleteView,DetailView
from django.urls import  reverse_lazy
from django.shortcuts import  redirect, render

from Cursos.forms import CursosForm, EspecialidadesForm

from trabajosC.models import  Cursos

# Create your views here.

class registrarCurso(CreateView):
    model = Cursos
    form_class= CursosForm
    template_name='createCurso.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):        
        context = {}
        context['title'] = 'Registrar Curso'
        context['form'] = self.form_class       

        return context

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.get_context_data())

class CursoUpdate(UpdateView):
    model = Cursos
    form_class = CursosForm
    template_name = 'curso_editModal.html'
    success_url = reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Editar Curso'
        context['cursos'] = Cursos.objects.all()        
        return context


class deleteCurso(DeleteView):
    model = Cursos
    template_name = 'curso_eliminarModal.html'

    def post(self, request,pk, *args, **kwargs):        
        object = Cursos.objects.get(id=pk)
        object.delete()
        return redirect('inicio')
 