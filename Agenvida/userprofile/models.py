#encoding:utf-8
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_countries import CountryField

# Create your models here.

SEXO_CHOICES=(
('FEMENINO', 'Femenino'),
('MASCULINO', 'Masculino'),
)

HORA_CHOICES=(
    ('MANANA', 'Mañana'),
    ('MEDIODIA', 'Mediodia'),
    ('TARDE', 'Tarde'),
    ('NOCHE', 'Noche'),
)

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    #avatar = AvatarField(upload_to="images/avatars/", width=100, height=100, blank=True, null=True)
    ideal_personal = models.CharField(max_length=140,null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True)
    sexo = models.CharField(max_length=15,null=True, choices=SEXO_CHOICES) ## poder elegir a traves de choices
    pais = CountryField()
    grupo_de_vida = models.CharField(max_length=140,null=True, blank=True)
    
    recordatorio= models.CharField(max_length=15,null=True, choices=HORA_CHOICES, default='MANANA')
    recordatorio_activo= models.BooleanField(default='True')
    
    


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class ContratoAutoeducacion(models.Model):
    user = models.ForeignKey(User, unique=True)
    afirmar = models.TextField(null=True)
    liberar = models.TextField(null=True)
    adquirir = models.TextField(null=True)

