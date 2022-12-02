from datetime import datetime
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView
from django.urls import  reverse_lazy
from django.views.generic.base import TemplateView
from django.db.models import Q,F, Sum
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import  redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin

from statistics import mean

from Evaluador.forms import RSyMAForm, casosyControlesForm, cohortesForm, eccForm, epForm, plantillaSCForm, plantillacorteTrasversalForm, pruebasDXForm
from Evaluador.models import plantillaCASOSyCONTROLES, plantillaCOHORTES, plantillaECC, plantillaEP, plantillaPruebasDX, plantillaRSyMA, plantillaSERIECASOS, plantillaCORTETRANSVERSAL

from trabajosC.models import Autores, Manuscritos, Trabajos, Trabajos_has_evaluadores, Tablas

# Create your views here.

class TrabajosAsignados(LoginRequiredMixin,TemplateView):
    """Clase TemplateView para ver la información de los trabajos científicos asignados al evaluador.

    **Context**    

        ``trabajos``:  Una instancia modelo del Trabajos creado en la app trabajosC`.

    **Template:**

        :template_name: Template para ver la información de los trabajos científicos.
    """
    model = Trabajos
    template_name = "trabajos_evaluador.html"
   
    def get_context_data(self, **kwargs):
        if self.request.user.is_superuser:
            Evaluador= Autores.objects.filter(role_id=2)
            context = super().get_context_data(**kwargs)
            context['trabajos'] = Trabajos_has_evaluadores.objects.all().select_related('trabajo')      
            context['manuscritos'] = Manuscritos.objects.select_related('trabajo')
            context['anexos'] = Tablas.objects.select_related('trabajo')
            context['plantillaECC'] = plantillaECC.objects.all().select_related('trabajo')
            context['plantillaPruebasDX'] = plantillaPruebasDX.objects.all().select_related('trabajo')
            context['plantillaRSyMA'] = plantillaRSyMA.objects.all().select_related('trabajo')
            context['plantillaSERIECASOS'] = plantillaSERIECASOS.objects.all().select_related('trabajo')
            context['plantillaCASOSyCONTROLES'] = plantillaCASOSyCONTROLES.objects.all().select_related('trabajo')
            context['plantillaCOHORTES'] = plantillaCOHORTES.objects.all().select_related('trabajo')
            context['plantillaCORTETRANSVERSAL'] = plantillaCORTETRANSVERSAL.objects.all().select_related('trabajo')
            context['plantillaEP'] = plantillaEP.objects.all().select_related('trabajo')

            return context
        else:
            Evaluador = Autores.objects.get(email = self.request.user.email)     
            context = super().get_context_data(**kwargs)
            context['trabajos'] = Trabajos_has_evaluadores.objects.filter(evaluador_id = Evaluador.id).select_related('trabajo')
            
            context['manuscritos'] = Manuscritos.objects.select_related('trabajo')
            context['anexos'] = Tablas.objects.select_related('trabajo')
            context['plantillaECC'] = plantillaECC.objects.filter(user=self.request.user).select_related('trabajo')
            context['plantillaPruebasDX'] = plantillaPruebasDX.objects.filter(user=self.request.user).select_related('trabajo')
            context['plantillaRSyMA'] = plantillaRSyMA.objects.filter(user=self.request.user).select_related('trabajo')
            context['plantillaSERIECASOS'] = plantillaSERIECASOS.objects.filter(user=self.request.user).select_related('trabajo')
            context['plantillaCASOSyCONTROLES'] = plantillaCASOSyCONTROLES.objects.filter(user=self.request.user).select_related('trabajo')
            context['plantillaCOHORTES'] = plantillaCOHORTES.objects.filter(user=self.request.user).select_related('trabajo')
            context['plantillaCORTETRANSVERSAL'] = plantillaCORTETRANSVERSAL.objects.filter(user=self.request.user).select_related('trabajo')
            context['plantillaEP'] = plantillaEP.objects.all().filter(user=self.request.user).select_related('trabajo')
            return context

class plantilla1_evaluacion(LoginRequiredMixin,UpdateView):
    ''' Clase UpdateView para realizar la evaluación de los TC. 

    **Context** 
       
        :model:  Una instancia de la plantilla ECC en donde se guardan los datos de la evaluación.
        :form_class:  Formulario para la realizar la evaluación del TC.
        :success_url:  Al ser exitoso la evaluación redirecciona al index del usuario.
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al formulario de realizar la evaluación.
    
    **Template:**

        :template_name: Template en donde está el formulario para la realizar la evaluación.
            
    '''    
    model = plantillaECC
    form_class = eccForm
    template_name = "plantillas_evaluacion/plantilla1.html"
    success_url = reverse_lazy('misEvaluaciones')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            trabajo_Evaluador = Trabajos_has_evaluadores.objects.filter(trabajo_id = self.object.trabajo_id)
            for obj in trabajo_Evaluador:
                if obj.evaluador.email == self.object.user.email:
                    d = form.cleaned_data
                    d.pop('comite_de_etica')
                    d.pop('registroClinica')
                    obj.comentario= d['comentario']
                    d.pop('comentario')
                    total = sum(d[x] for x in d) 
                    promedio = round(total*100/(len(d)*5), 2)
                    plantilla = form.save(commit=False)
                    plantilla.calificacion = promedio
                    plantilla.save()
                    obj.calificacion= promedio
                    obj.fecha_evaluacion= datetime.today()
                    obj.save()
                
            return redirect('misEvaluaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Realizar Evaluación'
        context['autores'] = Autores.objects.all()        
        return context

class plantilla2_evaluacion(LoginRequiredMixin,UpdateView):
    ''' Clase UpdateView para realizar la evaluación de los TC. 

    **Context** 
       
        :model:  Una instancia de la plantilla pruebasDX en donde se guardan los datos de la evaluación.
        :form_class:  Formulario para la realizar la evaluación del TC.
        :success_url:  Al ser exitoso la evaluación redirecciona al index del usuario.
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al formulario de realizar la evaluación.
    
    **Template:**

        :template_name: Template en donde está el formulario para la realizar la evaluación.
            
    '''

    model = plantillaPruebasDX
    form_class = pruebasDXForm
    template_name = "plantillas_evaluacion/plantilla2.html"
    success_url = reverse_lazy('misEvaluaciones')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            trabajo_Evaluador = Trabajos_has_evaluadores.objects.filter(trabajo_id = self.object.trabajo_id)
            for obj in trabajo_Evaluador:
                if obj.evaluador.email == self.object.user.email:
                    d = form.cleaned_data
                    d.pop('comite_de_etica')
                    obj.comentario= d['comentario']
                    d.pop('comentario')
                    total = sum(d[x] for x in d) 
                    promedio = round(total*100/(len(d)*5), 2)
                    plantilla = form.save(commit=False)
                    plantilla.calificacion = promedio
                    plantilla.save()
                    obj.calificacion= promedio
                    obj.fecha_evaluacion= datetime.today()
                    obj.save()
            
            return redirect('misEvaluaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Realizar Evaluación'
        context['autores'] = Autores.objects.all()        
        return context

class plantilla3_evaluacion(LoginRequiredMixin,UpdateView):
    ''' Clase UpdateView para realizar la evaluación de los TC. 

    **Context** 
       
        :model:  Una instancia de la plantilla RS y MA en donde se guardan los datos de la evaluación.
        :form_class:  Formulario para la realizar la evaluación del TC.
        :success_url:  Al ser exitoso la evaluación redirecciona al index del usuario.
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al formulario de realizar la evaluación.
    
    **Template:**

        :template_name: Template en donde está el formulario para la realizar la evaluación.
            
    '''

    model = plantillaRSyMA
    form_class = RSyMAForm
    template_name = "plantillas_evaluacion/plantilla3.html"
    success_url = reverse_lazy('misEvaluaciones')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            trabajo_Evaluador = Trabajos_has_evaluadores.objects.filter(trabajo_id = self.object.trabajo_id)
            for obj in trabajo_Evaluador:
                if obj.evaluador.email == self.object.user.email:
                    d = form.cleaned_data
                    d.pop('comite_de_etica')
                    obj.comentario= d['comentario']
                    d.pop('comentario')
                    total = sum(d[x] for x in d) 
                    promedio = round(total*100/(len(d)*5), 2)
                    plantilla = form.save(commit=False)
                    plantilla.calificacion = promedio
                    plantilla.save()
                    obj.calificacion= promedio
                    obj.fecha_evaluacion= datetime.today()
                    obj.save()
                
            return redirect('misEvaluaciones')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Realizar Evaluación'
        context['autores'] = Autores.objects.all()        
        return context

class plantilla4_evaluacion(LoginRequiredMixin,UpdateView):
    ''' Clase UpdateView para realizar la evaluación de los TC. 

    **Context** 
       
        :model:  Una instancia de la plantilla SERIECASOS en donde se guardan los datos de la evaluación.
        :form_class:  Formulario para la realizar la evaluación del TC.
        :success_url:  Al ser exitoso la evaluación redirecciona al index del usuario.
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al formulario de realizar la evaluación.
    
    **Template:**

        :template_name: Template en donde está el formulario para la realizar la evaluación.
            
    '''

    model = plantillaSERIECASOS
    form_class = plantillaSCForm
    template_name = "plantillas_evaluacion/plantilla4.html"
    success_url = reverse_lazy('misEvaluaciones')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            trabajo_Evaluador = Trabajos_has_evaluadores.objects.filter(trabajo_id = self.object.trabajo_id)
            for obj in trabajo_Evaluador:
                if obj.evaluador.email == self.object.user.email:
                    d = form.cleaned_data
                    d.pop('comite_de_etica')
                    obj.comentario= d['comentario']
                    d.pop('comentario')
                    total = sum(d[x] for x in d) 
                    promedio = round(total*100/(len(d)*5), 2)
                    plantilla = form.save(commit=False)
                    plantilla.calificacion = promedio
                    plantilla.save()
                    obj.calificacion= promedio
                    obj.fecha_evaluacion= datetime.today()
                    obj.save()
                
            return redirect('misEvaluaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Realizar Evaluación'
        context['autores'] = Autores.objects.all()        
        return context

class plantilla5_evaluacion(LoginRequiredMixin,UpdateView):
    ''' Clase UpdateView para realizar la evaluación de los TC. 

    **Context** 
       
        :model:  Una instancia de la plantilla CASOS y CONTROLES en donde se guardan los datos de la evaluación.
        :form_class:  Formulario para la realizar la evaluación del TC.
        :success_url:  Al ser exitoso la evaluación redirecciona al index del usuario.
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al formulario de realizar la evaluación.
    
    **Template:**

        :template_name: Template en donde está el formulario para la realizar la evaluación.
            
    '''

    model = plantillaCASOSyCONTROLES
    form_class = casosyControlesForm
    template_name = "plantillas_evaluacion/plantilla5.html"
    success_url = reverse_lazy('misEvaluaciones')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            trabajo_Evaluador = Trabajos_has_evaluadores.objects.filter(trabajo_id = self.object.trabajo_id)
            for obj in trabajo_Evaluador:
                if obj.evaluador.email == self.object.user.email:
                    d = form.cleaned_data
                    d.pop('comite_de_etica')
                    obj.comentario= d['comentario']
                    d.pop('comentario')
                    total = sum(d[x] for x in d) 
                    promedio = round(total*100/(len(d)*5), 2)
                    plantilla = form.save(commit=False)
                    plantilla.calificacion = promedio
                    plantilla.save()
                    obj.calificacion= promedio
                    obj.fecha_evaluacion= datetime.today()
                    obj.save()
                            
            return redirect('misEvaluaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Realizar Evaluación'
        context['autores'] = Autores.objects.all()        
        return context

class plantilla6_evaluacion(LoginRequiredMixin,UpdateView):
    ''' Clase UpdateView para realizar la evaluación de los TC. 

    **Context** 
       
        :model:  Una instancia de la plantilla COHORTES en donde se guardan los datos de la evaluación.
        :form_class:  Formulario para la realizar la evaluación del TC.
        :success_url:  Al ser exitoso la evaluación redirecciona al index del usuario.
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al formulario de realizar la evaluación.
    
    **Template:**

        :template_name: Template en donde está el formulario para la realizar la evaluación.
            
    '''

    model = plantillaCOHORTES
    form_class = cohortesForm
    template_name = "plantillas_evaluacion/plantilla6.html"
    success_url = reverse_lazy('misEvaluaciones')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            trabajo_Evaluador = Trabajos_has_evaluadores.objects.filter(trabajo_id = self.object.trabajo_id)
            for obj in trabajo_Evaluador:
                if obj.evaluador.email == self.object.user.email:
                    d = form.cleaned_data
                    d.pop('Comite_de_etica')
                    obj.comentario= d['comentario']
                    d.pop('comentario')
                    total = sum(d[x] for x in d) 
                    promedio = round(total*100/(len(d)*5), 2)
                    plantilla = form.save(commit=False)
                    plantilla.calificacion = promedio
                    plantilla.save()
                    obj.calificacion= promedio
                    obj.fecha_evaluacion= datetime.today()
                    obj.save()
                
            
            return redirect('misEvaluaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Realizar Evaluación'
        context['autores'] = Autores.objects.all()        
        return context

class plantilla7_evaluacion(LoginRequiredMixin,UpdateView):
    ''' Clase UpdateView para realizar la evaluación de los TC. 

    **Context** 
       
        :model:  Una instancia de la plantilla CORTETRANSVERSAL en donde se guardan los datos de la evaluación.
        :form_class:  Formulario para la realizar la evaluación del TC.
        :success_url:  Al ser exitoso la evaluación redirecciona al index del usuario.
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al formulario de realizar la evaluación.
    
    **Template:**

        :template_name: Template en donde está el formulario para la realizar la evaluación.
            
    '''

    model = plantillaCORTETRANSVERSAL
    form_class = plantillacorteTrasversalForm
    template_name = "plantillas_evaluacion/plantilla7.html"
    success_url = reverse_lazy('misEvaluaciones')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            trabajo_Evaluador = Trabajos_has_evaluadores.objects.filter(trabajo_id = self.object.trabajo_id)
            for obj in trabajo_Evaluador:
                if obj.evaluador.email == self.object.user.email:
                    d = form.cleaned_data
                    d.pop('comite_de_etica')
                    obj.comentario= d['comentario']
                    d.pop('comentario')
                    total = sum(d[x] for x in d) 
                    promedio = round(total*100/(len(d)*5), 2)
                    plantilla = form.save(commit=False)
                    plantilla.calificacion = promedio
                    plantilla.save()
                    obj.calificacion= promedio
                    obj.fecha_evaluacion= datetime.today()
                    obj.save()
                
            return redirect('misEvaluaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Realizar Evaluación'
        context['autores'] = Autores.objects.all()        
        return context
class plantillaEP_evaluacion(LoginRequiredMixin,UpdateView):
    ''' Clase UpdateView para realizar la evaluación de los TC. 

    **Context** 
       
        :model:  Una instancia de la plantilla de E-Poster en donde se guardan los datos de la evaluación.
        :form_class:  Formulario para la realizar la evaluación del TC.
        :success_url:  Al ser exitoso la evaluación redirecciona al index del usuario.
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al formulario de realizar la evaluación.
    
    **Template:**

        :template_name: Template en donde está el formulario para la realizar la evaluación.
            
    '''

    model = plantillaEP
    form_class = epForm
    template_name = "plantillas_evaluacion/plantillaEP.html"
    success_url = reverse_lazy('misEvaluaciones')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            trabajo_Evaluador = Trabajos_has_evaluadores.objects.filter(trabajo_id = self.object.trabajo_id)
            for obj in trabajo_Evaluador:
                if obj.evaluador.email == self.object.user.email:
                    d = form.cleaned_data
                    obj.comentario= d['comentario']
                    d.pop('comentario')
                    total = sum(d[x] for x in d) 
                    promedio = round(total*100/(len(d)*5), 2)
                    plantilla = form.save(commit=False)
                    plantilla.calificacion = promedio
                    plantilla.save()
                    obj.calificacion= promedio
                    obj.fecha_evaluacion= datetime.today()
                    obj.save()                
            
            return redirect('misEvaluaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Realizar Evaluación'
        context['autores'] = Autores.objects.all()        
        return context