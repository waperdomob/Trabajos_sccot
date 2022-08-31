from django.contrib.auth.decorators import login_required
from django.urls import path,include

from Cursos import views
from .views import *

urlpatterns = [
       
    path('create_Curso/', login_required(views.registrarCurso.as_view()), name='create_Curso'),
    path('edit_Curso/<int:pk>/', login_required(views.CursoUpdate.as_view()), name='edit_Curso'),
    path('delete_Curso/<int:pk>/', login_required(views.deleteCurso.as_view()), name='delete_Curso'),


]