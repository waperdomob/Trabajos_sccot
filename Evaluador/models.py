from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.conf import settings

from trabajosC.models import Trabajos
# Create your models here.

CALIFICACION = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),

    )
CHOICES = (
    ('SI', 'SI'),
    ('No', 'No')
)
class plantillaECC(models.Model):
    titulo=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Resumen_estructurado=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Palabras_claves=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_justificacion=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_objetivos = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    daprpi = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    pcmeISE = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    comite_de_etica=models.CharField(max_length=2,choices=CHOICES,blank=False, default='SI',help_text='Métodos')
    registroClinica=models.CharField(max_length=2,choices=CHOICES,blank=False, default='SI')
    doeEvP=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    dcve=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Tam_muestra =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    cdm=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    dca =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    dici=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    daijc=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Resultados')
    dcdp =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    rsapps=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    peprfce=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Discusión')
    sarclr =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    lrcdpcr =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    asevc =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    avear =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    calificacion = models.FloatField(null=True, blank=True)
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    objects = models.Manager()

class plantillaPruebasDX(models.Model):
    titulo=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Resumen_estructurado=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Palabras_claves=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_justificacion=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_objetivos = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    daprpi = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    comite_de_etica=models.CharField(max_length=2,choices=CHOICES,default='Si',blank=False, help_text='Métodos')
    ccpor=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    enmascaramiento=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    sappceaee=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Tam_muestra =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    srp=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    pecej=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Resultados')
    dcdp =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    rsapps=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    peprfce=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Discusión')
    sarclr =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    lrcdpcr =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    asevc =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    avear =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    calificacion = models.FloatField(null=True, blank=True)
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.trabajo.titulo

class plantillaRSyMA(models.Model):
    titulo=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Resumen_estructurado=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Palabras_claves=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_justificacion=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_objetivos = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    daprpi = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    comite_de_etica=models.CharField(max_length=2,choices=CHOICES,blank=False, default='SI',help_text='Métodos')
    dcepi=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    debPMBIM=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    dcdpep=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    dmeca =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    dmeh=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    dcme=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Resultados')
    dcdp =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    rsapps=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    peprfce=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Discusión')
    sarclr =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    lrcdpcr =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    asevc =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    avear =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    calificacion = models.FloatField(null=True, blank=True)
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    objects = models.Manager()

class plantillaSERIECASOSyCORTETRANSVERSAL(models.Model):
    titulo=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Resumen_estructurado=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Palabras_claves=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_justificacion=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_objetivos = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    daprpi = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    comite_de_etica=models.CharField(max_length=2,choices=CHOICES,blank=False,default='SI', help_text='Métodos')
    def_muestra=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    ecs=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    spsiGT=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    dve =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    pea=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Resultados')
    dcdp =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    rsapps=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    peprfce=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Discusión')
    sarclr =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    lrcdpcr =models.IntegerField(choices=CALIFICACION,default=1,blank=False,)
    asevc =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    avear =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    calificacion = models.FloatField(null=True, blank=True)
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.trabajo.titulo

class plantillaCASOSyCONTROLES(models.Model):
    titulo=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Resumen_estructurado=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Palabras_claves=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_justificacion=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_objetivos = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    daprpi = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    comite_de_etica=models.CharField(max_length=2,choices=CHOICES,blank=False, default='SI',help_text='Métodos')
    def_muestra=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    dsc=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    ecs=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    spsiGT=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    dve =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    ecvc =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    pea=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Resultados')
    dcdp =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    rsapps=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    peprfce=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Discusión')
    sarclr =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    lrcdpcr =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    asevc =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    avear =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    calificacion = models.FloatField(null=True, blank=True)
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.trabajo.titulo

class plantillaCOHORTES(models.Model):
    titulo=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Resumen_estructurado=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Palabras_claves=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_justificacion=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_objetivos = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    daprpi = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Comite_de_etica=models.CharField(max_length=2, choices=CHOICES,blank=False,default='SI', help_text='Métodos')
    dmr=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    mpddred=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    ecs=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    spsiGT=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    dve =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    ecvc =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    pea=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Resultados')
    dcdp =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    rsapps=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    peprfce=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Discusión')
    sarclr =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    lrcdpcr =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    asevc =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    avear =models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    calificacion = models.FloatField(null=True, blank=True)
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.trabajo.titulo

