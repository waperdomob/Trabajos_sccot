from django.contrib.auth.decorators import login_required
from django.urls import path,include

from Autores import views
from .views import *

urlpatterns = [
       
    path('create_Autor/', login_required(views.registrarAutor.as_view()), name='create_Autor'),
    path('edit_Autor/<int:pk>/', login_required(views.AutorUpdate.as_view()), name='edit_Autor'),
    path('delete_Autor/<int:pk>/', login_required(views.deleteAutor.as_view()), name='delete_Autor'),
    path('designarEvaluador/<int:pk>/',views.designarEvaluador,name='designarEvaluador'),
    path('eliminarEvaluador/<int:pk>/',views.eliminarEvaluador,name='eliminarEvaluador'),

]