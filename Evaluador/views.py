from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView
from django.views import View
from django.views.generic.base import TemplateView

from trabajosC.models import Autores, Manuscritos, Trabajos

# Create your views here.

class TrabajosAsignados(TemplateView):
    """Clase TemplateView para ver la información de los trabajos científicos asignados al evaluador.

    **Context**    

        ``trabajos``:  Una instancia modelo del Trabajos creado en la app trabajosC`.

    **Template:**

        :template_name: Template para ver la información de los trabajos científicos.
    """
    model = Trabajos
    template_name = "trabajos_evaluador.html"
   
    def get_context_data(self, **kwargs):   
        Evaluador = Autores.objects.get(email = self.request.user.email)     
        context = super().get_context_data(**kwargs)
        context['trabajos'] = Trabajos.objects.filter(evaluador = Evaluador)       
        context['manuscritos'] = Manuscritos.objects.filter(tituloM__icontains= 'pdf').select_related('trabajo')
        return context
   