from django.contrib import admin
from trabajosC import *
from trabajosC.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class institucionesAdmin(admin.ModelAdmin):
    list_display=("institucion",)

class rolesAdmin(admin.ModelAdmin):
    list_display=("role",)

class palabrasAdmin(ImportExportModelAdmin):
    list_display=("palabra",)
class keywordsAdmin(ImportExportModelAdmin):
    list_display=("keyword",)
class especialidadesAdmin(admin.ModelAdmin):
    list_display=("especialidad",)

class cursosAdmin(admin.ModelAdmin):
    list_display=("id","nombre_curso","especialidad","fecha_inicio","fecha_fin","ciudad",)


class autoresAdmin(ImportExportModelAdmin):
    list_display=("id","tipo_identificacion","identificacion","role","Nombres","Apellidos","miembro","email",)
class trabajos_has_autoresAdmin(admin.ModelAdmin):
    list_display=("id","trabajo","autor",)

class trabajos_has_institucionesAdmin(admin.ModelAdmin):
    list_display=("id","trabajo","institucion",)

class trabajos_has_palabrasAdmin(admin.ModelAdmin):
    list_display=("id","trabajo","palabra",)

class trabajos_has_evaluadoresAdmin(admin.ModelAdmin):
    list_display=("id","trabajo","evaluador","calificacion",)

class trabajos_has_keywordsAdmin(admin.ModelAdmin):
    list_display=("id","trabajo","keyword",)
class trabajosAdmin(admin.ModelAdmin):
    list_display=("id","identificador","tipo_trabajo","titulo","Autor_correspondencia","observaciones","fecha_subida","curso",)
    
class manusAdmin(admin.ModelAdmin):
    list_display=("tituloM","manuscrito","trabajo",)



admin.site.register(Instituciones,institucionesAdmin)
admin.site.register(Roles,rolesAdmin)
admin.site.register(Palabras_claves,palabrasAdmin)
admin.site.register(Keywords,keywordsAdmin)
admin.site.register(Especialidades,especialidadesAdmin)
admin.site.register(Cursos,cursosAdmin)
admin.site.register(Autores,autoresAdmin)
admin.site.register(Trabajos,trabajosAdmin)
admin.site.register(Manuscritos,manusAdmin)
admin.site.register(Trabajos_has_autores,trabajos_has_autoresAdmin)
admin.site.register(Trabajos_has_instituciones,trabajos_has_institucionesAdmin)
admin.site.register(Trabajos_has_palabras,trabajos_has_palabrasAdmin)
admin.site.register(Trabajos_has_Keywords,trabajos_has_keywordsAdmin)
admin.site.register(Trabajos_has_evaluadores,trabajos_has_evaluadoresAdmin)





