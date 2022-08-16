import sys
import subprocess
import re
from django.test import TestCase
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.wsgi import *
from djangoconvertvdoctopdf.convertor import StreamingConvertedPdf
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.core.files import File
from docx import Document
from trabajosC.models import Autores

manus_path = 'media/manuscritos/'

def send_email(nombre,usuario,password):    
    try:
        sent_to = "wilmer.a.p@hotmail.com"
        # Establecemos conexion con el servidor smtp de gmail
        mailServer = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        print("conectado..")
        # Construimos el mensaje simple
        mensaje = MIMEMultipart()
        mensaje['From']=settings.EMAIL_HOST_USER
        mensaje['To']=sent_to
        mensaje['Subject']="Evaluación Trabajo científico."
        
        content = render_to_string("emailEval.html", {'nombre': nombre, 'usuario':usuario, 'password':password,'link':'https://trabajos.sccot.org'+settings.LOGOUT_REDIRECT_URL})
        mensaje.attach(MIMEText(content,'html'))
        # Envio del mensaje
        mailServer.sendmail(settings.EMAIL_HOST_USER,
                        sent_to,
                        mensaje.as_string())
        print("Correo enviado correctamente")
    except Exception as e:
        print(e)

def crear_user():
    username_encontrado = False
    User = get_user_model()
    new_user = Autores.objects.get(id=2885)
    nombres = new_user.Nombres.lower().split()
    apellidos = new_user.Apellidos.lower().split()
    correo = new_user.email
    nombre_usuario = nombres[0][0]+nombres[1][0]+apellidos[0]+apellidos[1][0]
    contador = 0
    
    while username_encontrado == False:
        users = User.objects.filter(username = nombre_usuario)
        if users:
            nombre_usuario+=str(contador)
        else:
            username_encontrado = True
            print(nombre_usuario)
            print("prueba")
        contador +=1

    user_check = User.objects.filter(email = correo)
    if not user_check: 
        usuario = User(
            is_superuser=False,
            is_staff=False,
            username=nombre_usuario,
            first_name=new_user.Nombres,
            last_name=new_user.Apellidos,
            email=correo,
            is_active=True,
        )
        passwd = "TCsccot2022"
        usuario.set_password(passwd)
        send_email(new_user.Nombres, nombre_usuario, passwd)
        usuario.save()
    else:
        print("usuario existente")
#crear_user()
# Create your tests here.


def convert_to(folder, source, timeout=None):
    args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', folder, source]

    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    filename = re.search('-> (.*?) using filter', process.stdout.decode())

    if filename is None:
        raise LibreOfficeError(process.stdout.decode())
    else:
        return filename.group(1)


def libreoffice_exec():
    # TODO: Provide support for more platforms
    if sys.platform == 'darwin':
        return '/Applications/LibreOffice.app/Contents/MacOS/soffice'
    return 'libreoffice'


class LibreOfficeError(Exception):
    def __init__(self, output):
        self.output = output

convert_to('media/manuscritos',  'media/manuscritos/Ingreso86-docx', timeout=15)