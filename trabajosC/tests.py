from django.test import TestCase
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.wsgi import *
from django.core.mail import send_mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from trabajosC.models import Autores


def send_email():    
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
            
            content = render_to_string("emailEval.html")
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
    user_prueba = Autores.objects.get(id=2885)
    nombres = user_prueba.Nombres.lower().split()
    apellidos = user_prueba.Apellidos.lower().split()
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

    usuario = User(
            is_superuser=False,
            is_staff=False,
            username=nombre_usuario,
            first_name=user_prueba.Nombres,
            last_name=user_prueba.Apellidos,
            email=user_prueba.email,
            is_active=True,
        )
    passwd = "user_prb"
    usuario.set_password(passwd)
    #usuario.save()
crear_user()
# Create your tests here.
