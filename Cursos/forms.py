from django import forms
from django.db.models import Q

from trabajosC.models import Cursos, Especialidades

from .models import *
from django.forms import ModelForm

class CursosForm(ModelForm):
    class Meta:
        model= Cursos
        exclude = ('user',)

        labels = {
            'nombre_curso':'Nombre del curso',
        }
        widgets = {
	        'nombre_curso':forms.TextInput(attrs={'class':'form-control'}),
	        'especialidad':forms.Select(attrs={'class':'form-control'}),
            'fecha_inicio':forms.DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control','type': 'date'}),
            'fecha_fin':forms.DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control','type':'date'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
        }
                
class EspecialidadesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['especialidad'].widget.attrs['autofocus'] = True
        
    class Meta:
        model= Especialidades
        fields = '__all__'

        labels = {
            'especialidad':'Especialidad',
        }
        widgets = {
             'especialidad':forms.TextInput(attrs={'class': 'form-control select2'}),
        }
        
