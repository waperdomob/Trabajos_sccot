from unicodedata import name
from django.contrib.auth.decorators import login_required
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from Evaluador import views

urlpatterns = [
       
    path('misEvaluaciones/',login_required(views.TrabajosAsignados.as_view()), name='misEvaluaciones'),
    path('evaluar_Trabajo/<int:pk>/',login_required(views.TrabajosAsignados.as_view()),name='evaluar_trabajo'), 
    path('evaluacionECC/<int:pk>/',login_required(views.plantilla1_evaluacion.as_view()), name='evaluacionECC'),
    path('evaluacionPruebasDX/<int:pk>/',login_required(views.plantilla2_evaluacion.as_view()), name='evaluacionPruebasDX'),
    path('evaluacionRSyMA/<int:pk>/',login_required(views.plantilla3_evaluacion.as_view()), name='evaluacionRSyMA'),
    path('evaluacionSCyCT/<int:pk>/',login_required(views.plantilla4_evaluacion.as_view()), name='evaluacionSCyCT'),
    path('evaluacionCyC/<int:pk>/',login_required(views.plantilla5_evaluacion.as_view()), name='evaluacionCyC'),
    path('evaluacionCOHORTES/<int:pk>/',login_required(views.plantilla6_evaluacion.as_view()), name='evaluacionCOHORTES'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)