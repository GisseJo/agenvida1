#encoding:utf-8
from django import forms
from models import UserProfile, ContratoAutoeducacion
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = [  'ideal_personal','fecha_nacimiento', 'sexo','pais','grupo_de_vida'] 

class ContratoAutoeducacionForm(forms.ModelForm):
    afirmar= forms.CharField(label='¿Qué quiero afirmar en mi este año? - Aspectos positivos y valores que tengo', widget=forms.Textarea({'placeholder': 'Ej: Me consideran alegre entonces mi frase será: Nada me quitará la alegría'}))
    liberar= forms.CharField(label='¿De qué me quiero liberar? - Comportamientos negativos en mi personalidad que me impiden crecer',widget=forms.Textarea(attrs={'placeholder': 'Ej: Dejaré de compararme con los demás, entonces mi frase será: Soy original y Dios me ama como soy'}))
    adquirir= forms.CharField(label='¿Qué quiero adquirir para mi? - Actitudes y conductas que quiero conquistar',widget=forms.Textarea({'placeholder': 'Ej: Me gustaría crecer en la oración, entonces mi frase será: Todos los dias dialogo con Dios'}))
    
    class Meta:
        model = ContratoAutoeducacion
        fields = ('afirmar', 'liberar', 'adquirir')

class UserForm(forms.ModelForm):
    username= forms.CharField(help_text="")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

