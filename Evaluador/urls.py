from django.contrib.auth.decorators import login_required
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from Evaluador import views

urlpatterns = [
       
    path('misEvaluaciones/',login_required(views.TrabajosAsignados.as_view()), name='misEvaluaciones'),
    path('evaluar_Trabajo/<int:pk>/',login_required(views.TrabajosAsignados.as_view()),name='evaluar_trabajo'), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)