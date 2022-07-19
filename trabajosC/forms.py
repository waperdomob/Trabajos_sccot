from django import forms

from .models import *
from django.forms import ModelForm



CATEGORIAS = (
    ('Libre','Libre'),
    ('Ingreso','Ingreso'),
    ('E-poster','E-poster'),
)
SUBCATEGORIAS = (
    ('Investigacion clinica','Investigación clínica'),
    ('Ciencias basicas','Ciencias basicas'),
)
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
class SearchForm(forms.Form):
    documento = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Número del documento'}))

class AutoresForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Nombres'].widget.attrs['autofocus'] = True
        
    class Meta:
        model= Autores
        fields = '__all__'

        labels = {
            'tipo_identificacion' : 'Tipo de identificacion',
            'identificacion':'Identificacion',
            'role':'Rol',            

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
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
            'pais':forms.TextInput(attrs={'class':'form-control'}),
            'institucion':forms.TextInput(attrs={'class':'form-control'}),

        }
class AutoresForm2(ModelForm):

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Nombres'].widget.attrs['autofocus'] = True

    class Meta:
        model= Autores
        exclude = ('role',)

        labels = {
            'tipo_identificacion' : 'Tipo de identificacion',
            'identificacion':'Identificacion',

        }
        widgets = {
	        'tipo_identificacion':forms.TextInput(attrs={'class':'form-control'}),
            'identificacion':forms.TextInput(attrs={'class':'form-control'}),            
            'Nombres':forms.TextInput(attrs={'class':'form-control'}),
            'Apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'especialidad':forms.Select(attrs={'class':'form-control'}),
            'miembro':forms.Select(attrs={'class':'form-control'},choices=MIEMBROS),
            'email':forms.TextInput(attrs={'class':'form-control','type':'email'}),
            'celular':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
            'pais':forms.TextInput(attrs={'class':'form-control'}),
            'institucion':forms.TextInput(attrs={'class':'form-control'}),

        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class AutoresForm3(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Nombres'].widget.attrs['autofocus'] = True

    class Meta:
        model= Autores
        exclude = ['role','tipo_identificacion','identificacion','especialidad','celular','direccion','ciudad','pais']

        labels = {
            'tipo_identificacion' : 'Tipo de identificacion',
            'identificacion':'Identificacion',

        }
        widgets = {          
            'Nombres':forms.TextInput(attrs={'class':'form-control'}),
            'Apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'miembro':forms.Select(attrs={'class':'form-control'},choices=MIEMBROS),
            'email':forms.TextInput(attrs={'class':'form-control','type':'email'}),
            'institucion':forms.TextInput(attrs={'class':'form-control'}),

        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class CursosForm(ModelForm):
    class Meta:
        model= Cursos
        fields = '__all__'

        labels = {
            'nombre_curso':'Nombre del curso',
        }
        widgets = {
	        'nombre_curso':forms.TextInput(attrs={'class':'form-control'}),
	        'especialidad':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_inicio':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'fecha_fin':forms.DateInput(attrs={'class':'form-control','type': 'date'}),           
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}),
        }
        
        
class TrabajosCForm(ModelForm):

    class Meta:
        model= Trabajos
        exclude = ['fecha_inicio','fecha_fin','fecha_modificacion','evaluador','modificado_por']
        labels = {
            'tipo_trabajo':'Tipo de trabajo',
            'subtipo_trabajo':'subTipo',
            'Autor_correspondencia':'Autor Correspondencia',
            'otros_autores':'Autores',
            'titulo':'Titulo',
            'observaciones':'Observaciones',
            'institucion_principal':'Institucion principal',
            'resumen_esp':'Resumen en español',
            'palabras_claves':'Palabras claves',
            'resumen_ingles':'Resumen en ingles',
            'keywords':'Keywords',
            'curso':'Curso',
            'fecha_subida':'Fecha de subida',

        }
        widgets = {
            'tipo_trabajo':forms.Select(attrs={'class':'form-control'},choices=CATEGORIAS),
            'subtipo_trabajo':forms.Select(attrs={'class':'form-control'},choices=SUBCATEGORIAS),
	        'Autor_correspondencia':forms.Select(attrs={'class':'form-control select2'}),
	        'otros_autores':forms.SelectMultiple(attrs={'class':'form-control select2'}),
	        'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'observaciones':forms.TextInput(attrs={'class':'form-control'}),            
            'institucion_principal':forms.TextInput(attrs={'class':'form-control'}),
            'resumen_esp':forms.TextInput(attrs={'class':'form-control'}),
            'palabras_claves':forms.TextInput(attrs={'class':'form-control'}), 
            'resumen_ingles':forms.TextInput(attrs={'class':'form-control'}),
            'keywords':forms.TextInput(attrs={'class':'form-control '}),
	        'curso':forms.Select(attrs={'class':'form-control'}),
        }

class ManuscritosForm(ModelForm):
    class Meta:
        model= Manuscritos
        exclude = ['tituloM','trabajo']
        labels = {
            'manuscrito' : 'Manuscrito anónimo',
        }
        widgets = {          
            'manuscrito':forms.FileInput(attrs={'class':'form-control','multiple':True,'accept':"file_extension"}),
            
        }

class TablasForm(ModelForm):
    class Meta:
        model= Tablas
        exclude = ['tituloT','trabajo']
        labels = {
            'tabla' : 'Figuras, tablas, otros',
        }
        widgets = {          
            'tabla':forms.FileInput(attrs={'class': 'form-control','multiple':True}),
            
        }

class Trabajo_AutoresForm(ModelForm):
    class Meta:
        model= Trabajos_has_autores
        fields = '__all__'
        labels = {
            'trabajo' : 'Trabajo',
            'autor' : 'Autores',
        }
        widgets = {          
            'trabajo':forms.Select(attrs={'class': 'form-control select2','multiple':True}),
            'autor':forms.Select(attrs={'class': 'form-control select2','multiple':True}),
            
        }

class Trabajo_InstitucionesForm(ModelForm):
    class Meta:
        model= Trabajos_has_instituciones
        fields = '__all__'
        labels = {
            'trabajo' : 'Trabajo',
            'institucion' : 'Institucion',
        }
        widgets = {          
            'trabajo':forms.Select(attrs={'class': 'form-control','multiple':True}),
            'institucion':forms.Select(attrs={'class': 'form-control select2','multiple':True}),            
        }