
from trabajosC.models import Trabajos


def filtrar(curso,autor,institucion, tipoT):
    
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