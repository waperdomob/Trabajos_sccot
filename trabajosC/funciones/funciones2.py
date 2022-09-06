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
    """Función para guardar un mansucrito.

    Args:
        ruta (string): dirección (path) en donde se guardará el documento
        f (file): documento a guardar
    """    
    with open("media/"+ruta+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def email_confirmTC(nombre,correo,trabajo, curso):
    """Función para enviar correo de confirmación de recibido del trabajo científico.

    Args:
        nombre (string): Nombre del autor de correspondencia del TC
        correo (string): correo electrónico del autor de correspondencia del TC
        trabajo (string): Título del TC
        curso (string): Curso en el que se registró el TC
    """        
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
        
        content = render_to_string("emailConfirm.html", {'nombre': nombre, 'correosoporte':"revistacolombiana@sccot.org.co",'trabajo':trabajo, 'curso':curso})
        mensaje.attach(MIMEText(content,'html'))
        # Envio del mensaje
        mailServer.sendmail(settings.EMAIL_HOST_USER,
                        sent_to,
                        mensaje.as_string())
        print("Correo enviado correctamente")
    except Exception as e:
        print(e)

def send_emailEvaluador(nombre,usuario,password,correo):    
    """Función para enviar correo de asignación de evaluador.

    Args:
        nombre (string): Nombre del doctor asignado como evaluador.
        usuario (string): Usuario creado para que pueda acceder a la plataforma.
        password (string): Contraseña asignada al usuario.
        correo (string): correo del destinatario.
    """    
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

def send_emailEvaluador2(nombre,usuario,password,correo): 
    """Función para enviar correo en caso de que el usuario ya esté creado

    Args:
        nombre (string): Nombre del doctor asignado como evaluador
        usuario (string): Usuario para acceder a la plataforma
        correo (string): correo del destinatario.
    """       
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
        mensaje['Subject']="Evaluación Trabajo científico."
        
        content = render_to_string("emailEval2.html", {'nombre': nombre, 'usuario':usuario,'password':password,'link':'https://trabajos.sccot.org'+settings.LOGOUT_REDIRECT_URL,'correosporte':'revistacolombiana@sccot.org.co'})
        mensaje.attach(MIMEText(content,'html'))
        # Envio del mensaje
        mailServer.sendmail(settings.EMAIL_HOST_USER,
                        sent_to,
                        mensaje.as_string())
        print("Correo enviado correctamente")
    except Exception as e:
        print(e)

def crear_user(idEvaluador):
    """Función para crear un usuario. 

    Args:
        idEvaluador (int): id del doctor que será el evaluador de un TC.

    Returns:
        object: Objeto de la clase User que tendrá toda la información del usuario creado.
    """    
    username_encontrado = False
    User = get_user_model()
    new_user = Autores.objects.get(id=idEvaluador)
    nombres = new_user.Nombres.lower().split()
    apellidos = new_user.Apellidos.lower().split()
    correo = new_user.email

    if len(nombres) == 1 and len(apellidos)>=2:
        nombre_usuario = nombres[0:3]+apellidos[0]+apellidos[1][0]
    elif len(nombres) == 1 and len(apellidos)==1:
        nombre_usuario = nombres[0:3]+apellidos
    elif len(nombres) >= 2 and len(apellidos)==1:
        nombre_usuario = nombres[0][0]+nombres[1][0]+apellidos
    elif len(nombres) >=2 and len(apellidos)>=2:
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
        send_emailEvaluador(new_user.Nombres, nombre_usuario, passwd,correo)
        usuario.save()
        print("usuario creado.")
        return usuario
    else:
        passwd = "TCsccot2022"
        for value in user_check:
            send_emailEvaluador2(value.first_name, value.username,passwd,correo)
            print("usuario existente.")
            return value