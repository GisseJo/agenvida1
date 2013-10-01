from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    #avatar = models.ImageField("Profile Pic", upload_to="images/", blank=True, null=True)
    ideal_personal = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=50) ## poder elegir a traves de choices
    pais = models.CharField(max_length=50)
    grupo_de_vida = models.CharField(max_length=140)
    contrato_pedagogico = models.TextField() ## podria ser el atributo: unique_for_year

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  
 
post_save.connect(create_user_profile, sender=User) 
 
User.profile = property(lambda u: u.get_profile() )
#User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

#User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])