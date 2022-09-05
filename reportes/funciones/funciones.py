
from trabajosC.models import Trabajos


def filtrar(curso,autor,institucion, tipoT):
    """función para realizar el filtro en el modulo de reportes

    Args:
        curso (String): Nombre del curso.
        autor (String): Nombre del autor de correspondencia.
        institucion (String): Institución donde se realizó el trabajo científico.
        tipoT (String): Tipo de trabajo científico (Libre, Ingreso, E-poster)

    Returns:
        QuerySet: Lista de objectos del modelo trabajos.
    """    
    
    if tipoT != 'ninguna':
        search = Trabajos.objects.all().filter(tipo_trabajo=tipoT)
    else:
        search = Trabajos.objects.all()
    if curso and autor and institucion:            
        trabajos = search.filter(curso_id=curso).filter(Autor_correspondencia_id=autor).filter(institucion_principal_id=institucion)
    elif curso and institucion:
        trabajos = search.filter(curso_id=curso).filter(institucion_principal_id=institucion)
    elif curso and autor:
        trabajos = search.filter(curso_id=curso).filter(Autor_correspondencia_id=autor)
    elif autor and institucion:
        trabajos = search.filter(curso_id=curso).filter(Autor_correspondencia_id=autor)
    elif autor:
        trabajos = search.filter(Autor_correspondencia_id=autor)
    elif curso:
        trabajos = search.filter(curso_id=curso)
    elif institucion:
        trabajos = search.filter(institucion_principal_id=institucion)
    else: 
        trabajos=search

    return trabajos