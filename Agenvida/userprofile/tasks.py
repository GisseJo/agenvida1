# -*- coding: utf-8 -*-

from celery.task.schedules import crontab  
from celery.decorators import periodic_task  
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template ,render_to_string

# this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab  
@periodic_task(run_every=crontab(hour="6", minute="*", day_of_week="*"))  
def manana():      
    print "firing test task 1"   
    send_mail('Subject here', 'Here is the message. 1', 'from@example.com',
    ['rodri.valdez@gmail.com'], fail_silently=False)
    
@periodic_task(run_every=crontab(hour="12", minute="*/2", day_of_week="*"))      
def mediodia():      
    print "firing test task 2"   
    send_mail('Subject here', 'Here is the message 2.', 'from@example.com',
    ['rodri.valdez@gmail.com'], fail_silently=False)
    
@periodic_task(run_every=crontab(hour="16", minute="*", day_of_week="*"))      
def tarde():
          
    print "firing test task 2"   
    send_mail('Subject here', 'Here is the message 2.', 'from@example.com',
    ['rodri.valdez@gmail.com'], fail_silently=False)
    
    
@periodic_task(run_every=crontab(hour="20", minute="*", day_of_week="*"))      
def noche():      
    print "firing test task 2"   
    send_mail('Subject here', 'Here is the message 2.', 'from@example.com',
    ['rodri.valdez@gmail.com'], fail_silently=False)
    
@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))  
def test():      
    print "firing test task de prueba"
    
    
    subject = 'hello'
    from_email =  'hola@girolabs.com'
    to = '' 
    text_content = 'hola que tal! prueba de agenvida'
    html_content = get_template('email.html')
    html = render_to_string('email.html', {})
    bcc = ['rodri@girolabs.com','gisse@girolabs.com','hola@girolabs']
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to], bcc)
    msg.attach_alternative(html, 'text/html')
    msg.send()
      
@periodic_task(run_every=crontab(hour="1", minute="*", day_of_week="*"))      
def test2():      
    print "firing test task 2"   
    send_mail('Subject here', 'Here is the message 2.', 'from@example.com',
    ['rodri.valdez@gmail.com'], fail_silently=False)   
    
    
    