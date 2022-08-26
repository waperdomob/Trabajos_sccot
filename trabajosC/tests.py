from django.test import TestCase
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.wsgi import *
from djangoconvertvdoctopdf.convertor import StreamingConvertedPdf
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from trabajosC.models import Autores


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
        
        content = render_to_string("emailEval.html", {'nombre': nombre, 'usuario':usuario, 'password':password,'link':'https://trabajos.sccot.org'+settings.LOGOUT_REDIRECT_URL,'correosporte':'revistacolombiana@sccot.org.co'})
        mensaje.attach(MIMEText(content,'html'))
        # Envio del mensaje
        mailServer.sendmail(settings.EMAIL_HOST_USER,
                        sent_to,
                        mensaje.as_string())
        print("Correo enviado correctamente")
    except Exception as e:
        print(e)

def send_email2(nombre,usuario):    
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
        
        content = render_to_string("emailEval.html", {'nombre': nombre, 'usuario':usuario,'link':'https://trabajos.sccot.org'+settings.LOGOUT_REDIRECT_URL,'correosporte':'revistacolombiana@sccot.org.co'})
        mensaje.attach(MIMEText(content,'html'))
        # Envio del mensaje
        mailServer.sendmail(settings.EMAIL_HOST_USER,
                        sent_to,
                        mensaje.as_string())
        print("Correo enviado correctamente")
    except Exception as e:
        print(e)

def crear_user(idEvaluador):
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
        print("usuario creado.")

    else:
        send_email2(user_check.first_name, user_check.username)
        print("usuario existente.")
#crear_user()
# Create your tests here.