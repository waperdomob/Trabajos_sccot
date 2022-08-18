
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView,DeleteView
from django.urls import  reverse_lazy
from django.shortcuts import  redirect, render

from Autores.forms import AutoresForm

from trabajosC.models import Autores

# Create your views here.

class registrarAutor(CreateView):
    ''' Clase CreateView para registrar Autores. 

    **Context**

        :model: Una instancia del modelo Autores creado en la app trabajosC.
        :form_class: Formulario para la creación de autores creado en forms.py de la app Autores.

    **Methods**

        :``get(self, request, *args, **kwargs)``: 

            Metodo para redireccionar al template obteniendo el context de get_context_data.

        :``get_context_data(self, **kwargs)``: 

            Envio del context al formulario de crear autores.
    
    **Template:**

        :template_name: Formulario para la creación de un autor.
            
    '''
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
    ''' Clase UpdateView para actualizar los autores. 

    **Context** 
       
        :model:  Una instancia del modelo Autores creado en la app trabajosC.
        :form_class:  Formulario para la edición de autores creado en forms.py de la app Autores.
        :success_url:  Al ser exitoso la actualización del autor redirecciona al index.
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al formulario de editar autores.
    
    **Template:**

        :template_name: Formulario para la edición de un autor.
            
    '''
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
    ''' Clase DeleteView para eliminar los autores. 

    **Context**    

        :model:  Una instancia del modelo Autores creado en la app trabajosC.
        
    **Methods**
        
        :``post(self, request,pk, *args, **kwargs)``: 

            Metodo que recibe la información del autor a eliminar y al finalizar retorna al index.
    
    **Template:**

        :template_name: Formulario para la eliminación de un autor.
            
    '''
    model = Autores
    template_name = 'autor_eliminarModal.html'

    def post(self, request,pk, *args, **kwargs):        
        object = Autores.objects.get(id=pk)
        object.delete()
        return redirect('inicio')

def designarEvaluador(request,pk):
    """Le asigna el rol de evaluador a un autor

    **Args**
        :request (): Parametro necesario para realizar la actualización.
        :pk (number): id del autor.

    **Returns**
        :redirect: Redirecciona al index.
    """
    Autores.objects.filter(id = pk).update(role_id = 2)
    return redirect('inicio')

def eliminarEvaluador(request,pk):
    """Le quita el rol de evaluador a un autor

    **Args**
        :request (): Parametro necesario para realizar la actualización.
        :pk (number): id del autor.

    **Returns**
        :redirect: Redirecciona al index.
    """
    Autores.objects.filter(id = pk).update(role_id = None)
    return redirect('inicio')