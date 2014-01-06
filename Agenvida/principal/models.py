from django.db import models
from django.contrib.auth.models import User

class PropositoManager(models.Manager):
    def get_marcaciones_positivas(self):
        return self.filter(marcaciones__cumplimiento=1 ).count()
    
class Vinculacion(models.Model):
    vinculacion = models.CharField(max_length=50)
    
    def __unicode__(self):
        return unicode(self.vinculacion)
    
class Proposito(models.Model):
    usuario = models.ForeignKey(User,related_name='propositos' )
    vinculacion = models.ForeignKey(Vinculacion,related_name='propositos', blank=True, null=True )
    mes_ano = models.DateField()
    proposito = models.TextField()
    objects =PropositoManager ()
    def cant_marc_check(self):
        return self.marcaciones.filter(cumplimiento=1).count()
    
    def __unicode__(self):
        return unicode(self.proposito)
    
class Marcacion(models.Model):
    usuario = models.ForeignKey(User, related_name='marcaciones')
    proposito = models.ForeignKey(Proposito,related_name='marcaciones' )
    
    dia = models.DateField()
    cumplimiento = models.IntegerField()
    class Meta:
        ordering = ['dia'] # ordeno para el reporte del pdf
   
   
    def __unicode__(self):
        return unicode(self.cumplimiento)
    
class Tipo_marcacion(models.Model):
    tipo = models.CharField(max_length=50)
    RangoSup = models.IntegerField()
    RangoInf = models.IntegerField()
    
    def __unicode__(self):
        return unicode(self.tipo)
    
    
class PropositoParticular(models.Model):
    usuario = models.ForeignKey(User,related_name='pparticulares' )   
    mes_ano = models.DateField()
    nombre = models.TextField()
    
    def __unicode__(self):
        return unicode(self.nombre) 
    
    
    
    


