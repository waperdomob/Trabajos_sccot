from django import forms

from trabajosC.models import Autores, Cursos, Especialidades, Instituciones

CATEGORIAS = (
    ('ninguna','-------------'),
    ('Libre','Libre'),
    ('Ingreso','Ingreso'),
    ('E-poster','E-poster'),
)
class reportForm(forms.Form):
    required_css_class = 'textLabel'
    date_range = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off'
    }))    
    curso = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control select2'}))
    autor = forms.CharField(widget=forms.Select(attrs={'class': 'form-control select2'}))
    institucion = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control select2'}))
    tipoTrabajo = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control select2'}),choices=CATEGORIAS)
    