from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    avatar = models.ImageField("Profile Pic", upload_to="images/", blank=True, null=True)
    ideal_personal = models.TextField()
    user = models.ForeignKey(User, unique=True)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=50) ## poder elegir a traves de choices
    pais = models.CharField(max_length=50)
    grupo_de_vida = models.CharField(max_length=140)
    contrato_pedagogico = models.TextField() ## podria ser el atributo: unique_for_year
    
    def __unicode__(self):
        return unicode(self.user)
    
class Vinculacion(models.Model):
    vinculacion = models.CharField(max_length=50)
    
    def __unicode__(self):
        return unicode(self.vinculacion)
    
class Proposito(models.Model):
    usuario = models.ForeignKey(User,related_name='propositos' )
    vinculacion = models.ForeignKey(Vinculacion,related_name='propositos' )
    mes_ano = models.DateField()
    proposito = models.TextField()
    
    def __unicode__(self):
        return unicode(self.proposito)
    
class Marcacion(models.Model):
    usuario = models.ForeignKey(User, related_name='marcaciones')
    proposito = models.ForeignKey(Proposito,related_name='marcaciones' )
    
    dia = models.DateField()
    cumplimiento = models.IntegerField()
    
    def __unicode__(self):
        return unicode(self.cumplimiento)
    
class Tipo_marcacion(models.Model):
    tipo = models.CharField(max_length=50)
    RangoSup = models.IntegerField()
    RangoInf = models.IntegerField()
    
    def __unicode__(self):
        return unicode(self.tipo)
    
    
    
    


