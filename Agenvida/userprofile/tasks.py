# -*- coding: utf-8 -*-

from celery.task.schedules import crontab  
from celery.decorators import periodic_task  
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template ,render_to_string
from userprofile.models import UserProfile
from django.contrib.auth.models import User

# this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab  
@periodic_task(run_every=crontab(hour="6", minute="0", day_of_week="*"))  
def manana():      
    print "firing task MANANA"
    usuarios = User.objects.filter( userprofile__recordatorio='MANANA', userprofile__recordatorio_activo=True )
    print usuarios.query
    lista= []
    for usuario in usuarios:
        lista.append(usuario.email)
        
    subject = 'Acordate de tu Horario espiritual!'
    from_email =  ''
    to = '' 
    text_content = 'Acuertdate de completar tu horario espiritual! entra a www.agenvida.com/he'
    
    html = render_to_string('email.html', {})
    
    msg = EmailMultiAlternatives(subject, text_content, from_email,[to], lista)
    msg.attach_alternative(html, 'text/html')
    msg.send()

    
@periodic_task(run_every=crontab(hour="12", minute="0", day_of_week="*"))      
def mediodia(): 
    print "firing task MEDIODIA"
    usuarios = User.objects.filter( userprofile__recordatorio='MEDIODIA', userprofile__recordatorio_activo=True )
    print usuarios.query
    lista= []
    for usuario in usuarios:
        lista.append(usuario.email)
        
    subject = 'Acordate de tu Horario espiritual!'
    from_email =  ''
    to = '' 
    text_content = 'Acuertdate de completar tu horario espiritual! entra a www.agenvida.com/he'
    
    html = render_to_string('email.html', {})
    
    msg = EmailMultiAlternatives(subject, text_content, from_email,[to], lista)
    msg.attach_alternative(html, 'text/html')
    msg.send()

    
@periodic_task(run_every=crontab(hour="16", minute="0", day_of_week="*"))      
def tarde():
    print "firing task TARDE"
    usuarios = User.objects.filter( userprofile__recordatorio='TARDE', userprofile__recordatorio_activo=True )
    print usuarios.query
    lista= []
    for usuario in usuarios:
        lista.append(usuario.email)
        
    subject = 'Acordate de tu Horario espiritual!'
    from_email =  ''
    to = '' 
    text_content = 'Acuertdate de completar tu horario espiritual! entra a www.agenvida.com/he'
    
    html = render_to_string('email.html', {})
    
    msg = EmailMultiAlternatives(subject, text_content, from_email,[to], lista)
    msg.attach_alternative(html, 'text/html')
    msg.send()

    
@periodic_task(run_every=crontab(hour="20", minute="*", day_of_week="*"))      
def noche():      
    print "firing task NOCHE"
       
    usuarios = User.objects.filter( userprofile__recordatorio='NOCHE', userprofile__recordatorio_activo=True )
    print usuarios.query
    lista= []
    for usuario in usuarios:
        lista.append(usuario.email)
        
    subject = 'Acordate de tu Horario espiritual!'
    from_email =  ''
    to = '' 
    text_content = 'Acuertdate de completar tu horario espiritual! entra a www.agenvida.com/he'
    
    html = render_to_string('email.html', {})
    
    msg = EmailMultiAlternatives(subject, text_content, from_email,[to], lista)
    msg.attach_alternative(html, 'text/html')
    msg.send()

    
    
@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))  
def test():      
    print "firing prueba"
    
    
    usuarios = User.objects.filter( userprofile__recordatorio='NOCHE', userprofile__recordatorio_activo=True )
    print usuarios.query
    lista= []
    for usuario in usuarios:
        lista.append(usuario.email)
        
    subject = 'Acordate de tu Horario espiritual!'
    from_email =  ''
    to = '' 
    text_content = 'Acuertdate de completar tu horario espiritual! entra a www.agenvida.com/he'
    
    html = render_to_string('email.html', {})
    
    msg = EmailMultiAlternatives(subject, text_content, from_email,[to], lista)
    msg.attach_alternative(html, 'text/html')
    msg.send()

    
    
    