from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese sus nombres'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese sus apellidos'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese su email'}),
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese su username'}),
            'password': forms.PasswordInput(render_value=True,attrs={'class': 'form-control','placeholder': 'Ingrese su password'}),
            
        }
        exclude = ['user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff']

