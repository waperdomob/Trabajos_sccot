from django.contrib import admin
from Evaluador.models import *
# Register your models here.

class plantillaECCAdmin(admin.ModelAdmin):
    list_display=("calificacion","trabajo","user")

class plantillaPruebasDXAdmin(admin.ModelAdmin):
    list_display=("calificacion","trabajo","user")

class plantillaRSyMAAdmin(admin.ModelAdmin):
    list_display=("calificacion","trabajo","user")

class plantillaSERIECASOSAdmin(admin.ModelAdmin):
    list_display=("calificacion","trabajo","user")

class plantillaCORTETRANSAdmin(admin.ModelAdmin):
    list_display=("calificacion","trabajo","user")
class plantillaCASOSyCONTROLESAdmin(admin.ModelAdmin):
    list_display=("calificacion","trabajo","user")

class plantillaCOHORTESAdmin(admin.ModelAdmin):
    list_display=("calificacion","trabajo","user")

class plantillaEPOSTERAdmin(admin.ModelAdmin):
    list_display=("calificacion","trabajo","user")

admin.site.register(plantillaECC,plantillaECCAdmin)
admin.site.register(plantillaPruebasDX,plantillaPruebasDXAdmin)
admin.site.register(plantillaRSyMA,plantillaRSyMAAdmin)
admin.site.register(plantillaSERIECASOS,plantillaSERIECASOSAdmin)
admin.site.register(plantillaCORTETRANSVERSAL,plantillaSERIECASOSAdmin)
admin.site.register(plantillaCASOSyCONTROLES,plantillaCORTETRANSAdmin)
admin.site.register(plantillaCOHORTES,plantillaCOHORTESAdmin)
admin.site.register(plantillaEP,plantillaEPOSTERAdmin)
