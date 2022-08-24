from django import forms
from django.db.models import Q

from .models import *
from django.forms import ModelForm
from django import forms


CHOICES =(
    ("0","------------"),
    ("eccForm", "Plantilla ECC"),
    ("pruebasDXForm", "Plantilla pruebasDX"),
    ("RSyMAForm", "Plantilla RSyMA"),
    ("plantillaSCyCTForm", "Plantilla Serie casos y Corte Transversal"),
    ("casosyControlesForm", "Plantilla Casos y Controles"),
    ("cohortesForm", "Plantilla Cohortes"),
)

class eccForm(ModelForm):
    class Meta:
        model= plantillaECC
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Titulo',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripcion de justificacion',
            'Descripcion_de_objetivos': 'Descripcion de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'pcmeISE':'Presentación clara de manejo de equipoise',
            'comite_de_etica':'Comite de ética',
            'registroClinica':'Registrado en clinicaltrials.gov',
            'doeEvP':'Definición de orientación del estudio: explicativo vs. pragmático',
            'dcve':'Definición clara de variables de estudio',
            'Tam_muestra':'¿Justificado por variables de interés?',
            'cdm':'Cálculo descrito en el manuscrito',
            'dca':'Descripción clara de aleatorización',
            'dici':'Descripción de intervenciones clara - inequívoca',
            'daijc':'Definición de análisis interino, justificación, mecanismos',
            'dcdp':'Descripción completa de demografía de los participantes',
            'rsapps':'Reporte de sujetos que no aceptaron participar (cohortes y ECC) o se perdieron en el seguimiento',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura mas reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'pcmeISE':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'registroClinica':forms.Select(attrs={'class':'form-control'}),
            'doeEvP':forms.Select(attrs={'class':'form-control'}),
            'dcve':forms.Select(attrs={'class':'form-control'}),
            'Tam_muestra':forms.Select(attrs={'class':'form-control'}),
            'cdm':forms.Select(attrs={'class':'form-control'}),
            'dca':forms.Select(attrs={'class':'form-control'}),
            'dici':forms.Select(attrs={'class':'form-control'}),
            'daijc':forms.Select(attrs={'class':'form-control'}),
            'dcdp':forms.Select(attrs={'class':'form-control'}),
            'rsapps':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            
        }

class pruebasDXForm(ModelForm):
    class Meta:
        model= plantillaPruebasDX
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Titulo',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripcion de justificacion',
            'Descripcion_de_objetivos': 'Descripcion de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'comite_de_etica':'Comite de ética',
            'ccpor':'¿Comparación con un patron de oro reconocido?',
            'enmascaramiento':'¿Hubo enmascaramiento?',
            'sappceaee':'¿Se aplicó las pruebas en una población con espectro amplio de la enfermedad de estudio?',
            'Tam_muestra':'¿Tamaño de la muestra explicado?',
            'srp':'¿Se repitieron las pruebas?',
            'pecej':'¿Pruebas estadísticas claramente explicadas y justificadas?',
            'dcdp':'Descripción completa de demografía de los participantes',
            'rsapps':'Reporte de sujetos que no aceptaron participar (cohortes y ECC) o se perdieron en el seguimiento',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura mas reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'ccpor':forms.Select(attrs={'class':'form-control'}),
            'enmascaramiento':forms.Select(attrs={'class':'form-control'}),
            'sappceaee':forms.Select(attrs={'class':'form-control'}),
            'Tam_muestra':forms.Select(attrs={'class':'form-control'}),
            'srp':forms.Select(attrs={'class':'form-control'}),
            'pecej':forms.Select(attrs={'class':'form-control'}),
            'dcdp':forms.Select(attrs={'class':'form-control'}),
            'rsapps':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            
        }

class RSyMAForm(ModelForm):
    class Meta:
        model= plantillaRSyMA
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Titulo',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripcion de justificacion',
            'Descripcion_de_objetivos': 'Descripcion de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'comite_de_etica':'Comite de ética',
            'dcepi':'Definición clara y explícita de preguntas de investigación',
            'debPMBIM':'Descripción de estrategia de búsqueda: palabras, Mesh, bases de datos, idiomas, marco de tiempo',
            'dcdpep':'Descripción clara de proceso de depuración',
            'dmeca':'Descripción de métodos de evaluación de calidad de artículos',
            'dmeh':'Descripción de métodos de evaluación de homogeneidad',
            'dcme':'Descripción clara de métodos estadísticos',
            'dcdp':'Descripción completa de demografía de los participantes',
            'rsapps':'Reporte de sujetos que no aceptaron participar (cohortes y ECC) o se perdieron en el seguimiento',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura mas reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'dcepi':forms.Select(attrs={'class':'form-control'}),
            'debPMBIM':forms.Select(attrs={'class':'form-control'}),
            'dcdpep':forms.Select(attrs={'class':'form-control'}),
            'dmeca':forms.Select(attrs={'class':'form-control'}),
            'dmeh':forms.Select(attrs={'class':'form-control'}),
            'dcme':forms.Select(attrs={'class':'form-control'}),
            'dcdp':forms.Select(attrs={'class':'form-control'}),
            'rsapps':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            
        }

class plantillaSCyCTForm(ModelForm):
    class Meta:
        model= plantillaSERIECASOSyCORTETRANSVERSAL
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Titulo',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripcion de justificacion',
            'Descripcion_de_objetivos': 'Descripcion de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'comite_de_etica':'Comite de ética',
            'def_muestra':'Definición de la muestra: tamaño y probabilística vs conveniencia',
            'ecs':'Estrategia de control de sesgos',
            'spsiGT':'Seguimiento (Porcentaje de sujetos incluidos/grupo total)',
            'dve':'Definición de variables estudiadas',
            'pea':'¿Pruebas estadísticas adecuadas?',
            'dcdp':'Descripción completa de demografía de los participantes',
            'rsapps':'Reporte de sujetos que no aceptaron participar (cohortes y ECC) o se perdieron en el seguimiento',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura mas reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'def_muestra':forms.Select(attrs={'class':'form-control'}),
            'ecs':forms.Select(attrs={'class':'form-control'}),
            'spsiGT':forms.Select(attrs={'class':'form-control'}),
            'dve':forms.Select(attrs={'class':'form-control'}),
            'pea':forms.Select(attrs={'class':'form-control'}),
            'dcdp':forms.Select(attrs={'class':'form-control'}),
            'rsapps':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            
        }

class casosyControlesForm(ModelForm):
    class Meta:
        model= plantillaCASOSyCONTROLES
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Titulo',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripcion de justificacion',
            'Descripcion_de_objetivos': 'Descripcion de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'comite_de_etica':'Comite de ética',
            'def_muestra':'Definición de la muestra: tamaño y probabilística vs conveniencia',
            'dsc':'Descripción de selección de controles',
            'ecs':'Estrategia de control de sesgos',
            'spsiGT':'Seguimiento (Porcentaje de sujetos incluidos/grupo total)',
            'dve':'Definición de variables estudiadas',
            'ecvc':'Estrategias para control de variables de confusión',
            'pea':'¿Pruebas estadísticas adecuadas?',
            'dcdp':'Descripción completa de demografía de los participantes',
            'rsapps':'Reporte de sujetos que no aceptaron participar (cohortes y ECC) o se perdieron en el seguimiento',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura mas reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'def_muestra':forms.Select(attrs={'class':'form-control'}),
            'dsc':forms.Select(attrs={'class':'form-control'}),
            'ecs':forms.Select(attrs={'class':'form-control'}),
            'spsiGT':forms.Select(attrs={'class':'form-control'}),
            'dve':forms.Select(attrs={'class':'form-control'}),
            'ecvc':forms.Select(attrs={'class':'form-control'}),
            'pea':forms.Select(attrs={'class':'form-control'}),
            'dcdp':forms.Select(attrs={'class':'form-control'}),
            'rsapps':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            
        }

class cohortesForm(ModelForm):
    class Meta:
        model= plantillaCOHORTES
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Titulo',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripcion de justificacion',
            'Descripcion_de_objetivos': 'Descripcion de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'Comite_de_etica':'Comite de ética',
            'dmr':'Descripción de método de reclutamiento',
            'mpddred':'Mecanismos para definición y detección de riesgo, exposición y desenlaces',
            'ecs':'Estrategia de control de sesgos',
            'spsiGT':'Seguimiento (Porcentaje de sujetos incluidos/grupo total)',
            'dve':'Definición de variables estudiadas',
            'ecvc':'Estrategias para control de variables de confusión',
            'pea':'¿Pruebas estadísticas adecuadas?',
            'dcdp':'Descripción completa de demografía de los participantes',
            'rsapps':'Reporte de sujetos que no aceptaron participar (cohortes y ECC) o se perdieron en el seguimiento',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura mas reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'Comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'dmr':forms.Select(attrs={'class':'form-control'}),
            'mpddred':forms.Select(attrs={'class':'form-control'}),
            'ecs':forms.Select(attrs={'class':'form-control'}),
            'spsiGT':forms.Select(attrs={'class':'form-control'}),
            'dve':forms.Select(attrs={'class':'form-control'}),
            'ecvc':forms.Select(attrs={'class':'form-control'}),
            'pea':forms.Select(attrs={'class':'form-control'}),
            'dcdp':forms.Select(attrs={'class':'form-control'}),
            'rsapps':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            
        }

class selectPlantillaForm(forms.Form):
    required_css_class = 'textLabel'
    plantilla = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),label="Plantillas de calificación",choices=CHOICES)