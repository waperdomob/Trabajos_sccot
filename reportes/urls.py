from django.contrib.auth.decorators import login_required
from django.urls import path,include

from reportes import views
from .views import *

urlpatterns = [
       
    path('', views.reporteTC.as_view(), name='reportes'),
    

]