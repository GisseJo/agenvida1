from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    #avatar = models.ImageField("Profile Pic", upload_to="images/", blank=True, null=True)
    ideal_personal = models.CharField(max_length=50,null=True)
    fecha_nacimiento = models.DateField(null=True)
    sexo = models.CharField(max_length=50,null=True) ## poder elegir a traves de choices
    pais = models.CharField(max_length=50,null=True)
    grupo_de_vida = models.CharField(max_length=140,null=True)
    contrato_pedagogico = models.TextField(null=True) ## podria ser el atributo: unique_for_year


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

#User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])