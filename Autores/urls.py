from django.contrib.auth.decorators import login_required
from django.urls import path,include

from Autores import views
from .views import *

urlpatterns = [
       
    path('create_Autor/', views.registrarAutor.as_view(), name='create_Autor'),
    path('edit_Autor/<int:pk>/', views.AutorUpdate.as_view(), name='edit_Autor'),
    path('delete_Autor/<int:pk>/', views.deleteAutor.as_view(), name='delete_Autor'),
    path('designarEvaluador/<int:pk>/',views.designarEvaluador,name='designarEvaluador'),
    path('eliminarEvaluador/<int:pk>/',views.eliminarEvaluador,name='eliminarEvaluador'),

]