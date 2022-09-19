import subprocess
from subprocess import  Popen
from django.conf import settings

from Evaluador.forms import eccForm
from Evaluador.models import plantillaCASOSyCONTROLES, plantillaCOHORTES, plantillaECC, plantillaPruebasDX, plantillaRSyMA, plantillaSERIECASOS, plantillaEP, plantillaCORTETRANSVERSAL

LIBRE_OFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"

def convert_to_pdf_wd(input_docx, out_folder):
    """Función para convertir word a pdf desde windows

    Args:
        input_docx (string): ruta y nombre del documento a convertir
        out_folder (string): ruta en donde se guardará el nuevo doc pdf
    """    
    p = Popen([LIBRE_OFFICE, '--headless', '--convert-to', 'pdf', '--outdir',
               out_folder, input_docx])
    print([LIBRE_OFFICE, '--convert-to', 'pdf', input_docx])
    p.communicate()


def generate_pdf_linux(doc_path, path, timeout=None):
    """Función para convertir word a pdf desde linux

    Args:
        doc_path (string): ruta y nombre del documento a convertir
        out_folder (string): ruta en donde se guardará el nuevo doc pdf
    """  
    args = ['libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', path, doc_path]

    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)

def asignar_plantilla(nombre,Trabajo, User):
    
    if nombre == "eccForm":
        plantillaECC.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "pruebasDXForm":
        plantillaPruebasDX.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "RSyMAForm":
        plantillaRSyMA.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "plantillaSCForm":
        plantillaSERIECASOS.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "plantillaCTForm":
        plantillaCORTETRANSVERSAL.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "casosyControlesForm":
        plantillaCASOSyCONTROLES.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "cohortesForm":
        plantillaCOHORTES.objects.create(trabajo=Trabajo, user= User)
    else:
        plantillaEP.objects.create(trabajo=Trabajo, user= User)