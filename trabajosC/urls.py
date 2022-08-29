from django.contrib.auth.decorators import login_required
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from trabajosC import views

urlpatterns = [
       
    path('',views.index, name='inicio'),
    re_path('^ajax_especialidades/$', views.ajax_especialidades, name='ajax_especialidades'),
    path('create_Trabajo/', views.registrarTrabajo.as_view(), name='create_Trabajo'),
    path('Detalle_Trabajo/<int:pk>/',login_required(views.TrabajoDetailView.as_view()), name='detalleTrabajo'),
    path('evaluador_Trabajo/<int:pk>/',login_required(views.AsignarEvaluadorTC.as_view()), name='asignarEvaluador'),
    path('editar_manuscrito/<int:pk>/', views.ManuscritoEdit.as_view(), name='editar_manuscrito'),
    path('Trabajo/sacar_promedio/<int:pk>/',views.promedioTC, name='promediarEvaluacion')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)