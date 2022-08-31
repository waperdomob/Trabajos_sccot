from django.contrib.auth.decorators import login_required
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from reportes import views

urlpatterns = [
       
    path('', login_required(views.reporteTC.as_view()), name='reportes'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)