
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.conf import settings

# Create your models here.

CATEGORIAS = [
    ('Libre','Libre'),
    ('Ingreso','Ingreso'),
    ('E-poster','E-poster'),
]
SUBCATEGORIAS = [
    ('Investigacion clinica','Investigación clínica'),
    ('Ciencias basicas','Ciencias basicas'),
]
ROLES = [
    ('autor_correspondencia','autor_correspondencia'),
    ('Evaluador','Evaluador'),
    ]
    

class Roles(models.Model):
    """
    Roles asignados a los autores, estos pueden ser: autor_correspondencia o evaluador.
    """
    role = models.CharField(max_length=45, choices=ROLES)
    def __str__(self):
        return self.role

class Instituciones(models.Model):
    """
    Instituciones que se registrarán en el trabajo científico.
    """
    institucion = models.CharField(max_length=45)

    def __str__(self):
        return self.institucion

    def toJSON(self):
        item = model_to_dict(self)
        item['institucion'] = self.institucion
        return item

class Especialidades(models.Model):
    """
    Especialidades de los autores(doctores).
    """
    especialidad = models.CharField(max_length=45)
    def __str__(self):
        return self.especialidad

    def toJSON(self):
        item = model_to_dict(self)
        item['especialidad'] = self.especialidad
        return item

class Cursos(models.Model):
    """
    Cursos disponibles para subir el trabajo científico.
    """
    nombre_curso = models.CharField(max_length=45)
    especialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin_evaluacion = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField()
    ciudad = models.CharField(max_length=45)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_curso+" "+self.fecha_fin.strftime("%d %B, %Y")

    def toJSON(self):
        item = model_to_dict(self)
        item['nombre_curso'] = self.nombre_curso
        return item   
class Autores(models.Model):
    """
    Doctores miembros de la Sccot que serán autores de trabajos científicos.
    """
    tipo_identificacion = models.CharField(max_length=45,null=True, blank=True)
    identificacion = models.CharField(max_length=45,null=True, blank=True)
    role = models.ForeignKey(Roles,null=True, blank=True, on_delete=models.CASCADE)
    Nombres = models.CharField(max_length=60)
    Apellidos = models.CharField(max_length=60)
    especialidad = models.ForeignKey(Especialidades,null=True, blank=True, on_delete=models.CASCADE)
    miembro = models.CharField(max_length=45,null=True, blank=True)
    email = models.CharField(max_length=100)
    celular = models.CharField(max_length=100,null=True, blank=True)
    direccion = models.CharField(max_length=200,null=True, blank=True)
    ciudad = models.CharField(max_length=45,null=True, blank=True)
    pais = models.CharField(max_length=45,null=True, blank=True)
    institucion = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{} {} '.format(self.Nombres, self.Apellidos)

    def toJSON(self):
        item = model_to_dict(self)   
        item['full_name'] = self.get_full_name()

        return item

class Trabajos(models.Model):
    """
    Trabajos científicos subidos por los doctores. 
    """
    identificador = models.CharField(max_length=45,null=True,blank=True)
    tipo_trabajo=models.CharField(max_length=45, choices=CATEGORIAS)
    subtipo_trabajo=models.CharField(max_length=45, choices=SUBCATEGORIAS,null=True, blank=True)
    titulo=models.CharField(max_length=100)
    Autor_correspondencia=models.ForeignKey(Autores, on_delete=models.CASCADE)
    observaciones=models.TextField(null=True, blank=True)
    institucion_principal=models.ForeignKey(Instituciones, on_delete=models.CASCADE)
    resumen_esp=models.TextField()
    resumen_ingles=models.TextField()
    fecha_subida = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateField('ultima modificacion',auto_now= True,null=True, blank=True)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    calificacion = models.FloatField(null=True, blank=True)
    modificado_por = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo

class Trabajos_has_evaluadores(models.Model):
    """
    Relación Many to Many entre trabajo y evaluadores(autores con role evaluador). 
    """
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE,  blank=True, null=True)
    evaluador = models.ForeignKey(Autores, on_delete=models.CASCADE, blank=True, null=True)
    calificacion = models.FloatField(null=True, blank=True)
    comentario=models.TextField(null=True, blank=True)
    fecha_evaluacion = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.trabajo.titulo
        
class Trabajos_has_autores(models.Model):
    """
    Relación Many to Many entre trabajo y autores. 
    """
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE, blank=True, null=True)
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.trabajo.titulo
        
class Trabajos_has_instituciones(models.Model):
    """
    Relación Many to Many entre trabajo e instituciones. 
    """
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE, blank=True, null=True)
    institucion = models.ForeignKey(Instituciones, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.trabajo.titulo

class Manuscritos(models.Model):
    """
    Documento relacionado al trabajo científico:
        - Word si es libre o ingreso
        - Powerpoint o video si es E-poster
    """
    tituloM = models.CharField(max_length=100)
    manuscrito  = models.FileField()
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    def __str__(self):
        return self.tituloM

class Tablas(models.Model):
    """
    Documentos adicionales del trabajo científico.
    """
    tituloT = models.CharField(max_length=100)
    tabla  = models.FileField(null=True, blank=True,)
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    def __str__(self):
        return self.tituloT

class Palabras_claves(models.Model):
    """
    Palabras claves usadas en el trabajo científico. También se usarán como buscador para la siguiente fase del proyecto.
    """
    palabra = models.CharField(max_length=45)

    def __str__(self):
        return self.palabra

    def toJSON(self):
        item = model_to_dict(self)
        item['palabra'] = self.palabra
        return item

class Trabajos_has_palabras(models.Model):
    """
    Relación Many to Many entre trabajo y palabras claves. 
    """
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE, blank=True, null=True)
    palabra = models.ForeignKey(Palabras_claves, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.palabra.palabra

class Keywords(models.Model):
    """
    Keywords usadas en el trabajo científico. También se usarán como buscador para la siguiente fase del proyecto.
    """
    keyword = models.CharField(max_length=45)

    def __str__(self):
        return self.keyword

    def toJSON(self):
        item = model_to_dict(self)
        item['keyword'] = self.keyword
        return item

class Trabajos_has_Keywords(models.Model):
    """
    Relación Many to Many entre trabajo y keywords. 
    """
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE, blank=True, null=True)
    keyword = models.ForeignKey(Keywords, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.keyword.keyword