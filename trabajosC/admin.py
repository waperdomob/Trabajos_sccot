from django.contrib import admin
from trabajosC import *
from trabajosC.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class institucionesAdmin(admin.ModelAdmin):
    list_display=("institucion",)

class rolesAdmin(admin.ModelAdmin):
    list_display=("role",)

class especialidadesAdmin(admin.ModelAdmin):
    list_display=("especialidad",)

class cursosAdmin(admin.ModelAdmin):
    list_display=("nombre_curso","especialidad","fecha_inicio","fecha_fin","ciudad",)


class autoresAdmin(ImportExportModelAdmin):
    list_display=("id","tipo_identificacion","identificacion","role","Nombres","Apellidos","miembro","email",)

class trabajosAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "otros_autores":
            kwargs["queryset"] = Trabajos.objects.filter(titulo=request.user)
        return super().formfield_for_dbfield(db_field, request, **kwargs)
    
class manusAdmin(admin.ModelAdmin):
    list_display=("tituloM","manuscrito","trabajo",)



admin.site.register(Instituciones,institucionesAdmin)
admin.site.register(Roles,rolesAdmin)
admin.site.register(Especialidades,especialidadesAdmin)
admin.site.register(Cursos,cursosAdmin)
admin.site.register(Autores,autoresAdmin)
admin.site.register(Trabajos,trabajosAdmin)
admin.site.register(Manuscritos,manusAdmin)


