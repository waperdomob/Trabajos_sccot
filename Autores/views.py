import datetime as dtime
from django.http import JsonResponse
from django.db.models import Q

from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView,DeleteView,DetailView
from django.urls import  reverse_lazy
from django.shortcuts import  redirect, render

from Autores.forms import AutoresForm

from trabajosC.models import Autores, Cursos, Instituciones, Trabajos, Trabajos_has_autores

# Create your views here.

class registrarAutor(CreateView):
    model = Autores
    form_class= AutoresForm
    template_name='createAutor.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):        
        context = {}
        context['title'] = 'Registrar Autor'
        context['form'] = self.form_class

        return context

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.get_context_data())

class AutorUpdate(UpdateView):
    model = Autores
    form_class = AutoresForm
    template_name = 'autor_editModal.html'
    success_url = reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Editar Autor'
        context['autores'] = Autores.objects.all()        
        return context

class deleteAutor(DeleteView):
    model = Autores
    template_name = 'autor_eliminarModal.html'

    def post(self, request,pk, *args, **kwargs):        
        object = Autores.objects.get(id=pk)
        object.delete()
        return redirect('inicio')

def designarEvaluador(request,pk):

    Autores.objects.filter(id = pk).update(role_id = 2)
    return redirect('inicio')

def eliminarEvaluador(request,pk):
    Autores.objects.filter(id = pk).update(role_id = None)
    return redirect('inicio')