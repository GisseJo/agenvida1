from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_countries import CountryField

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    #avatar = AvatarField(upload_to="images/avatars/", width=100, height=100, blank=True, null=True)
    ideal_personal = models.CharField(max_length=50,null=True)
    fecha_nacimiento = models.DateField(null=True)
    sexo = models.CharField(max_length=50,null=True) ## poder elegir a traves de choices
    pais = CountryField()
    grupo_de_vida = models.CharField(max_length=140,null=True)
    contrato_pedagogico = models.TextField(null=True) ## podria ser el atributo: unique_for_year


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

