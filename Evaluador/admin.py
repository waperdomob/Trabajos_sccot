from django.contrib import admin
from Evaluador.models import *
# Register your models here.

class plantillaECCAdmin(admin.ModelAdmin):
    list_display=("calificacion","trabajo","user")

class plantillaPruebasDXAdmin(admin.ModelAdmin):
    list_display=("calificacion","trabajo","user")

class plantillaRSyMAAdmin(admin.ModelAdmin):
    list_display=("calificacion","trabajo","user")

class plantillaSERIECASOSyCORTETRANSVERSALAdmin(admin.ModelAdmin):
    list_display=("calificacion","trabajo","user")

class plantillaCASOSyCONTROLESAdmin(admin.ModelAdmin):
    list_display=("calificacion","trabajo","user")

class plantillaCOHORTESAdmin(admin.ModelAdmin):
    list_display=("calificacion","trabajo","user")

admin.site.register(plantillaECC,plantillaECCAdmin)
admin.site.register(plantillaPruebasDX,plantillaPruebasDXAdmin)
admin.site.register(plantillaRSyMA,plantillaRSyMAAdmin)
admin.site.register(plantillaSERIECASOSyCORTETRANSVERSAL,plantillaSERIECASOSyCORTETRANSVERSALAdmin)
admin.site.register(plantillaCASOSyCONTROLES,plantillaCASOSyCONTROLESAdmin)
admin.site.register(plantillaCOHORTES,plantillaCOHORTESAdmin)