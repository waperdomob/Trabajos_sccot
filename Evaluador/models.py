from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.conf import settings

from trabajosC.models import Trabajos
# Create your models here.

CALIFICACION = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),

    )
CHOICES = (
    (5, 'SI'),
    (1, 'No')
)
class plantillaECC(models.Model):
    titulo=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Resumen_estructurado=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Palabras_claves=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_justificacion=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_objetivos = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    daprpi = models.IntegerField(choices=CALIFICACION,default=1,blank=False,help_text='Diseño adecuado para responder pregunta de investigación')
    pcmeISE = models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Presentación clara de manejo de equipoise')
    Comite_de_etica=models.IntegerField(choices=CHOICES,blank=False)
    metodos=models.IntegerField(choices=CHOICES,blank=False, help_text='Registrado en clinicaltrials.gov')
    doeEvP=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Definición de orientación del estudio: explicativo vs. pragmático')
    dcve=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Definición clara de variables de estudio')
    Tam_muestra =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Tamaño de muestra')
    jvi=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='¿Justificado por variables de interés?')
    cdm=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Cálculo descrito en el manuscrito')
    dca =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción clara de aleatorización')
    dici=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción de intervenciones clara - inequívoca')
    daijc=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Definición de análisis interino, justificación, mecanismos.')
    dcdp =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción completa de demografía de los participantes')
    rsapps=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Reporte de sujetos que no aceptaron participar (cohortes y ECC) o se perdieron en el seguimiento.')
    peprfce=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita.')
    sarclr =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Suficiente análisis de los resultados, comparación con la literatura mas reciente.')
    lrcdpcr =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Las referencias citadas son discutidas y puestas en contexto con los resultados.')
    asevc =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Análisis de sesgos, efecto de variables de confusión.')
    avear =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Análisis de la validez externa (aplicabilidad) de los resultados.')
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.trabajo.titulo

class plantillaPruebasDX(models.Model):
    titulo=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Resumen_estructurado=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Palabras_claves=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_justificacion=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_objetivos = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    daprpi = models.IntegerField(choices=CALIFICACION,default=1,blank=False,help_text='Diseño adecuado para responder pregunta de investigación')
    Comite_de_etica=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    metodos=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='¿Comparación con un patron de oro reconocido?')
    enmascaramiento=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='¿Hubo enmascaramiento?')
    sappceaee=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='¿Se aplicó las pruebas en una población con espectro amplio de la enfermedad de estudio?')
    Tam_muestra =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='¿Tamaño de la muestra explicado?')
    srp=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='¿Se repitieron las pruebas?')
    pecej=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='¿Pruebas estadísticas claramente explicadas y justificadas?')
    dcdp =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción completa de demografía de los participantes')
    rsapps=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Reporte de sujetos que no aceptaron participar (cohortes y ECC) o se perdieron en el seguimiento.')
    peprfce=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita.')
    sarclr =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Suficiente análisis de los resultados, comparación con la literatura mas reciente.')
    lrcdpcr =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Las referencias citadas son discutidas y puestas en contexto con los resultados.')
    asevc =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Análisis de sesgos, efecto de variables de confusión.')
    avear =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Análisis de la validez externa (aplicabilidad) de los resultados.')
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
    daprpi = models.IntegerField(choices=CALIFICACION,default=1,blank=False,help_text='Diseño adecuado para responder pregunta de investigación')
    Comite_de_etica=models.IntegerField(choices=CHOICES,blank=False)
    metodos=models.IntegerField(choices=CALIFICACION,blank=False, help_text='Definición clara y explícita de preguntas de investigación.')
    debPMBIM=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción de estrategia de búsqueda: palabras, Mesh, bases de datos, idiomas, marco de tiempo.')
    dcdpep=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción clara de proceso de depuración.')
    dmeca =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción de métodos de evaluación de calidad de artículos.')
    dmeh=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción de métodos de evaluación de homogeneidad.')
    dcme=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción clara de métodos estadísticos.')
    dcdp =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción completa de demografía de los participantes')
    rsapps=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Reporte de sujetos que no aceptaron participar (cohortes y ECC) o se perdieron en el seguimiento.')
    peprfce=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita.')
    sarclr =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Suficiente análisis de los resultados, comparación con la literatura mas reciente.')
    lrcdpcr =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Las referencias citadas son discutidas y puestas en contexto con los resultados.')
    asevc =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Análisis de sesgos, efecto de variables de confusión.')
    avear =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Análisis de la validez externa (aplicabilidad) de los resultados.')
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.trabajo.titulo

class plantillaSERIECASOSyCOHORTESTRANSVERSALES(models.Model):
    titulo=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Resumen_estructurado=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Palabras_claves=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_justificacion=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_objetivos = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    daprpi = models.IntegerField(choices=CALIFICACION,default=1,blank=False,help_text='Diseño adecuado para responder pregunta de investigación')
    Comite_de_etica=models.IntegerField(choices=CHOICES,blank=False)
    ddmtpc=models.IntegerField(choices=CALIFICACION,blank=False, help_text='Definición de la muestra: tamaño y probabilística vs conveniencia.')
    ecs=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Estrategia de control de sesgos.')
    spsiGT=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Seguimiento (Porcentaje de sujetos incluidos/grupo total).')
    dve =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Definición de variables estudiadas.')
    pea=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='¿Pruebas estadísticas adecuadas?.')
    dcdp =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción completa de demografía de los participantes')
    rsapps=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Reporte de sujetos que no aceptaron participar (cohortes y ECC) o se perdieron en el seguimiento.')
    peprfce=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita.')
    sarclr =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Suficiente análisis de los resultados, comparación con la literatura mas reciente.')
    lrcdpcr =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Las referencias citadas son discutidas y puestas en contexto con los resultados.')
    asevc =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Análisis de sesgos, efecto de variables de confusión.')
    avear =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Análisis de la validez externa (aplicabilidad) de los resultados.')
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
    daprpi = models.IntegerField(choices=CALIFICACION,default=1,blank=False,help_text='Diseño adecuado para responder pregunta de investigación')
    Comite_de_etica=models.IntegerField(choices=CHOICES,blank=False)
    ddmtpc=models.IntegerField(choices=CALIFICACION,blank=False, help_text='Definición de la muestra: tamaño y probabilística vs conveniencia.')
    dsc=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción de selección de controles.')
    ecs=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Estrategia de control de sesgos.')
    spsiGT=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Seguimiento (Porcentaje de sujetos incluidos/grupo total).')
    dve =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Definición de variables estudiadas.')
    ecvc =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Estrategias para control de variables de confusión.')
    pea=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='¿Pruebas estadísticas adecuadas?.')
    dcdp =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción completa de demografía de los participantes')
    rsapps=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Reporte de sujetos que no aceptaron participar (cohortes y ECC) o se perdieron en el seguimiento.')
    peprfce=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita.')
    sarclr =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Suficiente análisis de los resultados, comparación con la literatura mas reciente.')
    lrcdpcr =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Las referencias citadas son discutidas y puestas en contexto con los resultados.')
    asevc =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Análisis de sesgos, efecto de variables de confusión.')
    avear =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Análisis de la validez externa (aplicabilidad) de los resultados.')
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.trabajo.titulo

class plantillaCOHORTESLONGITUDINALES(models.Model):
    titulo=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Resumen_estructurado=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Palabras_claves=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_justificacion=models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    Descripcion_de_objetivos = models.IntegerField(choices=CALIFICACION,default=1,blank=False)
    daprpi = models.IntegerField(choices=CALIFICACION,default=1,blank=False,help_text='Diseño adecuado para responder pregunta de investigación')
    pcmeISE = models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Presentación clara de manejo de equipoise')
    Comite_de_etica=models.IntegerField(choices=CHOICES,blank=False)
    ddmtpc=models.IntegerField(choices=CALIFICACION,blank=False, help_text='Definición de la muestra: tamaño y probabilística vs conveniencia.')
    dmr=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción de método de reclutamiento.')
    mpddred=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Mecanismos para definición y detección de riesgo, exposición y desenlaces.')
    ecs=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Estrategia de control de sesgos.')
    spsiGT=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Seguimiento (Porcentaje de sujetos incluidos/grupo total).')
    dve =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Definición de variables estudiadas.')
    ecvc =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Estrategias para control de variables de confusión.')
    pea=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='¿Pruebas estadísticas adecuadas?.')
    dcdp =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Descripción completa de demografía de los participantes')
    rsapps=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Reporte de sujetos que no aceptaron participar (cohortes y ECC) o se perdieron en el seguimiento.')
    peprfce=models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita.')
    sarclr =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Suficiente análisis de los resultados, comparación con la literatura mas reciente.')
    lrcdpcr =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Las referencias citadas son discutidas y puestas en contexto con los resultados.')
    asevc =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Análisis de sesgos, efecto de variables de confusión.')
    avear =models.IntegerField(choices=CALIFICACION,default=1,blank=False, help_text='Análisis de la validez externa (aplicabilidad) de los resultados.')
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.trabajo.titulo
