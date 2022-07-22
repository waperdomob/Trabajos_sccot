from django.contrib.auth.decorators import login_required
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from trabajosC import views
from .views import *

urlpatterns = [
       
    path('',views.index, name='inicio'),
    re_path('^ajax_especialidades/$', views.ajax_especialidades, name='ajax_especialidades'),
    path('trabajos/create_Trabajo/', views.registrarTrabajo.as_view(), name='create_Trabajo'),
    path('trabajos/create_PDF/<int:pk>/', views.TrabajosPDF.as_view(), name='create_PDF'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)