
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView,DeleteView
from django.urls import  reverse_lazy
from django.shortcuts import  redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin

from Cursos.forms import CursosForm

from trabajosC.models import  Cursos
from usuario.mixins import IsSuperuserMixin
# Create your views here.

class registrarCurso(LoginRequiredMixin,IsSuperuserMixin,CreateView):
    ''' Clase CreateView para registrar los cursos. 

    **Context**

        :model: Una instancia del modelo Cursos creado en la app trabajosC.
        :form_class: Formulario para la creación de cursos creado en forms.py de la app Cursos.

    **Methods**

        :``get(self, request, *args, **kwargs)``: 

            Metodo para redireccionar al template obteniendo el context de get_context_data.

        :``get_context_data(self, **kwargs)``: 

            Envio del context al formulario de crear cursos.
    
    **Template:**

        :template_name: Formulario para la creación de un curso.
            
    '''
    model = Cursos
    form_class= CursosForm
    template_name='createCurso.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        curso = CursosForm(request.POST)
        user_id=int(self.request.session.get('_auth_user_id'))
        if curso.is_valid():
            new_curso = curso.save(commit=False)
            new_curso.user_id = user_id
            new_curso.estado = True
            new_curso.save()
            return redirect('inicio')

    def get_context_data(self, **kwargs):        
        context = {}
        context['title'] = 'Registrar Curso'
        context['form'] = self.form_class       

        return context

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.get_context_data())

class CursoUpdate(LoginRequiredMixin,IsSuperuserMixin,UpdateView):
    ''' Clase UpdateView para actualizar los cursos. 

    **Context** 
       
        :model:  Una instancia del modelo Cursos creado en la app trabajosC.
        :form_class:  Formulario para la edición de cursos creado en forms.py de la app Cursos.
        :success_url:  Al ser exitoso la actualización del curso redirecciona al index.
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al formulario de editar cursos.
    
    **Template:**

        :template_name: Formulario para la edición de un curso.
            
    '''
    model = Cursos
    form_class = CursosForm
    template_name = 'curso_editModal.html'
    success_url = reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Editar Curso'
        context['cursos'] = Cursos.objects.all()        
        return context


class deleteCurso(LoginRequiredMixin,IsSuperuserMixin,DeleteView):
    ''' Clase DeleteView para eliminar los cursos. 

    **Context**    

        :model:  Una instancia del modelo Cursos creado en la app trabajosC.
        
    **Methods**
        
        :``post(self, request,pk, *args, **kwargs)``: 

            Metodo que recibe la información del curso a eliminar y al finalizar retorna al index.
    
    **Template:**

        :template_name: Formulario para la eliminación de un curso.
            
    '''
    model = Cursos
    template_name = 'curso_eliminarModal.html'

    def post(self, request,pk, *args, **kwargs):        
        object = Cursos.objects.get(id=pk)
        object.delete()
        return redirect('inicio')
