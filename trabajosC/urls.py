from django.contrib.auth.decorators import login_required
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from trabajosC import views
from .views import *

urlpatterns = [
       
    path('',views.index, name='inicio'),
    path('create_Trabajo/', views.registrarTrabajo.as_view(), name='create_Trabajo'),
    path('create_autor/',views.create_autor, name='registrarAutor'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)