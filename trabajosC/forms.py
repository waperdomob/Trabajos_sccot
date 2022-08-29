from django import forms
from django.db.models import Q

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
    palabras_cl = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese una palabra'}))
    keyword_ls = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter a word'}))

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
            'Nombres':forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingrese su nombre completo'}),
            'Apellidos':forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingrese su apellido completo'}),
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
                aut = form.clean()
                autores = Autores.objects.filter(Q(email__icontains=aut['email']))
                if autores:
                    data['error'] = 'No es posible registrar el autor, ya existe'
                else:
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
            'Nombres':forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingrese su nombre completo'},),
            'Apellidos':forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingrese su apellido completo'}),
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

class InstitucionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['institucion'].widget.attrs['autofocus'] = True
        
    class Meta:
        model= Instituciones
        fields = '__all__'

        labels = {
            'institucion':'Institución',
        }
        widgets = {
             'institucion':forms.TextInput(attrs={'class': 'form-control '}),
        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                inst = form.clean()
                instituciones = Instituciones.objects.filter(Q(institucion__icontains=inst['institucion']))
                if instituciones:
                    data['error'] = 'No es posible registrar la institución, ya existe'
                else:
                    instance = form.save()
                    data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class Palabras_clavesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['palabra'].widget.attrs['autofocus'] = True
        
    class Meta:
        model= Palabras_claves
        fields = '__all__'

        labels = {
            'palabra':'Palabra clave',
        }
        widgets = {
             'palabra':forms.TextInput(attrs={'class': 'form-control '}),
        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                palb = form.clean()
                palabras = Palabras_claves.objects.filter(Q(palabra__icontains=palb['palabra']))
                if palabras:
                    data['error'] = 'No es posible registrar la palabra clave, ya existe'
                else:
                    instance = form.save()
                    data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class KeywordForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['keyword'].widget.attrs['autofocus'] = True
        
    class Meta:
        model= Keywords
        fields = '__all__'

        labels = {
            'keyword':'Keyword',
        }
        widgets = {
             'keyword':forms.TextInput(attrs={'class': 'form-control '}),
        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                inst = form.clean()
                keywords = Keywords.objects.filter(Q(keyword__icontains=inst['keyword']))
                if keywords:
                    data['error'] = 'No es posible registrar la keyword, ya existe'
                else:
                    instance = form.save()
                    data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class TrabajosCForm(ModelForm):

    class Meta:
        model= Trabajos
        exclude = ['fecha_inicio','fecha_fin','fecha_modificacion','evaluador','modificado_por']
        labels = {
            'tipo_trabajo':'Tipo de trabajo',
            'subtipo_trabajo':'Subtipo',
            'Autor_correspondencia':'Autor de correspondencia',
            'titulo':'Título',
            'observaciones':'Observaciones',
            'institucion_principal':'Institución principal del trabajo',
            'resumen_esp':'Resumen en español',
            'resumen_ingles':'Resumen en ingles',
            'curso':'Curso',
            'fecha_subida':'Fecha de subida',

        }
        widgets = {
            'tipo_trabajo':forms.Select(attrs={'class':'form-control'},choices=CATEGORIAS),
            'subtipo_trabajo':forms.Select(attrs={'class':'form-control'},choices=SUBCATEGORIAS),
	        'Autor_correspondencia':forms.Select(attrs={'class':'form-control select2'}),
	        'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'observaciones':forms.TextInput(attrs={'class':'form-control'}),            
            'institucion_principal':forms.Select(attrs={'class':'form-control select2'}),
            'resumen_esp':forms.TextInput(attrs={'class':'form-control'}),
            'resumen_ingles':forms.TextInput(attrs={'class':'form-control'}),
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
            'manuscrito':forms.FileInput(attrs={'class':'form-control','accept':"file_extension"}),
            
        }

class TablasForm(ModelForm):
    class Meta:
        model= Tablas
        exclude = ['tituloT','trabajo']
        labels = {
            'tabla' : 'Otros',
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
            'institucion' : 'Otras instituciones',
        }
        widgets = {          
            'trabajo':forms.Select(attrs={'class': 'form-control select2','multiple':True}),
            'institucion':forms.Select(attrs={'class': 'form-control select2','multiple':True}),  
        }

class Trabajo_PalabrasForm(ModelForm):
    class Meta:
        model= Trabajos_has_palabras
        fields = '__all__'
        labels = {
            'trabajo' : 'Trabajo',
            'palabra' : 'Palabras Claves',
        }
        widgets = {          
            'trabajo':forms.Select(attrs={'class': 'form-control select2','multiple':True}),
            'palabra':forms.Select(attrs={'class': 'form-control select2','multiple':True, 'readonly':True}),            
        }

class Trabajo_KeywordsForm(ModelForm):
    class Meta:
        model= Trabajos_has_Keywords
        fields = '__all__' 
        labels = {
            'trabajo' : 'Trabajo',
            'keyword' : 'Keywords',
        }
        widgets = {          
            'trabajo':forms.Select(attrs={'class': 'form-control select2','multiple':True}),
            'keyword':forms.Select(attrs={'class': 'form-control select2','multiple':True, 'readonly':True}),            
        }

class EvaluadorTrabajoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['evaluador'].queryset = Autores.objects.filter(role=2)
    class Meta:
        model= Trabajos_has_evaluadores
        fields = '__all__'
        labels = {
            'trabajo' : 'Trabajo',
            'evaluador' : 'Evaluador',
        }
        widgets = {          
            'trabajo':forms.Select(attrs={'class': 'form-control select2'}),
            'evaluador':forms.Select(attrs={'class': 'form-control select2'}),            
        }