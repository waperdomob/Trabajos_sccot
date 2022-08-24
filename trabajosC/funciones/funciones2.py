from django.test import TestCase
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.wsgi import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from trabajosC.models import Autores

def handle_uploaded_file(ruta,f):
    with open("media/"+ruta+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def email_confirmTC(nombre,correo,trabajo):    
    try:
        sent_to = correo
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
        mensaje['Subject']="Trabajo científico Recibido."
        
        content = render_to_string("emailConfirm.html", {'nombre': nombre, 'correosoporte':"revistacolombiana@sccot.org.co",'trabajo':trabajo})
        mensaje.attach(MIMEText(content,'html'))
        # Envio del mensaje
        mailServer.sendmail(settings.EMAIL_HOST_USER,
                        sent_to,
                        mensaje.as_string())
        print("Correo enviado correctamente")
    except Exception as e:
        print(e)