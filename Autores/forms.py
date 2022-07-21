from django import forms
from django.db.models import Q

from trabajosC.models import Autores

from .models import *
from django.forms import ModelForm


ROLES = (
    ('-------------','-------------'),
    ('autor_correspondencia','autor_correspondencia'),
    ('Evaluador','Evaluador'),
)
MIEMBROS = (
    ('-------------','-------------'),
    ('Si','Si'),
    ('No','No'),
)

class AutoresForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Nombres'].widget.attrs['autofocus'] = True
        
    class Meta:
        model= Autores
        fields = '__all__'

        labels = {
            'tipo_identificacion' : 'Tipo de Identificacion',
            'identificacion':'Identificacion',
            'role':'Rol', 
            'celular':'Celular',             

        }
        widgets = {
	        'tipo_identificacion':forms.TextInput(attrs={'class':'form-control'}),
            'identificacion':forms.TextInput(attrs={'class':'form-control'}),            
            'role':forms.Select(attrs={'class':'form-control'},choices=ROLES),
            'Nombres':forms.TextInput(attrs={'class':'form-control'}),
            'Apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'especialidad':forms.Select(attrs={'class':'form-control'}),
            'miembro':forms.Select(attrs={'class':'form-control'},choices=MIEMBROS),
            'email':forms.TextInput(attrs={'class':'form-control','type':'email'}),
            'celular':forms.NumberInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
            'pais':forms.TextInput(attrs={'class':'form-control'}),
            'institucion':forms.TextInput(attrs={'class':'form-control'}),

        }