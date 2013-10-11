from django import forms
from models import UserProfile, ContratoAutoeducacion


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = [  'ideal_personal','fecha_nacimiento', 'sexo','pais','grupo_de_vida'] 

class ContratoAutoeducacionForm(forms.ModelForm):
    afirmar= forms.CharField(label='Que quiero afirmar en mi este anho - Aspectos positivos valores que tengo',help_text='Ej Me consideran alegre entonces mi frase: Nada me quitara la alegria', widget=forms.Textarea)
    liberar= forms.CharField(label='De que me quiero liberar - Comportamientos negativos en mi personalidad que me impiden crecer',help_text='Ej Dejare de compararme con los demas entonces mi frase Soy original y Dios me ama como soy', widget=forms.Textarea)
    adquirir= forms.CharField(label='Que quiero adquirir para mi - Actitudes y conductas que quiero conquistar',help_text='Ej Ej Me gustaria crecer en la oracion entonces mi frase Todos los dias dialogo con Dios', widget=forms.Textarea)
    
    class Meta:
        model = ContratoAutoeducacion
        fields = ('afirmar', 'liberar', 'adquirir')

