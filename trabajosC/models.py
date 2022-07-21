
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
    role = models.CharField(max_length=45, choices=ROLES)
    def __str__(self):
        return self.role

class Instituciones(models.Model):
    institucion = models.CharField(max_length=45)

    def __str__(self):
        return self.institucion

    def toJSON(self):
        item = model_to_dict(self)
        item['institucion'] = self.institucion
        return item

class Especialidades(models.Model):
    especialidad = models.CharField(max_length=45)
    def __str__(self):
        return self.especialidad

    def toJSON(self):
        item = model_to_dict(self)
        item['especialidad'] = self.especialidad
        return item


class Cursos(models.Model):
    nombre_curso = models.CharField(max_length=45)
    especialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ciudad = models.CharField(max_length=45)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_curso
        
class Autores(models.Model):
    tipo_identificacion = models.CharField(max_length=45,null=True, blank=True)
    identificacion = models.BigIntegerField(null=True, blank=True)
    role = models.ForeignKey(Roles,null=True, blank=True, on_delete=models.CASCADE)
    Nombres = models.CharField(max_length=45)
    Apellidos = models.CharField(max_length=45)
    especialidad = models.ForeignKey(Especialidades,null=True, blank=True, on_delete=models.CASCADE)
    miembro = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    celular = models.BigIntegerField(null=True, blank=True)
    direccion = models.CharField(max_length=60,null=True, blank=True)
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
    tipo_trabajo=models.CharField(max_length=45, choices=CATEGORIAS)
    subtipo_trabajo=models.CharField(max_length=45, choices=SUBCATEGORIAS,null=True, blank=True)
    titulo=models.CharField(max_length=100)
    Autor_correspondencia=models.ForeignKey(Autores, on_delete=models.CASCADE)
    observaciones=models.CharField(max_length=100,null=True, blank=True)
    institucion_principal=models.ForeignKey(Instituciones, on_delete=models.CASCADE)
    resumen_esp=models.CharField(max_length=100)
    palabras_claves=models.CharField(max_length=100)
    resumen_ingles=models.CharField(max_length=100)
    keywords=models.CharField(max_length=100)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateField('ultima modificacion',null=True, blank=True)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    evaluador = models.ForeignKey(Autores,null=True, blank=True, on_delete=models.CASCADE,related_name='+')
    modificado_por = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo

class Trabajos_has_autores(models.Model):
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE, blank=True, null=True)
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.trabajo.titulo

class Manuscritos(models.Model):
    tituloM = models.CharField(max_length=100)
    manuscrito  = models.FileField(upload_to='manuscritos/',default="")
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    def __str__(self):
        return self.tituloM

class Tablas(models.Model):
    tituloT = models.CharField(max_length=100)
    tabla  = models.FileField(upload_to='tablas/',default="",null=True, blank=True,)
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    def __str__(self):
        return self.tituloT