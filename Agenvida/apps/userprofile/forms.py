from django import forms
from models import UserProfile


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = [  'ideal_personal','fecha_nacimiento', 'sexo','pais','grupo_de_vida'] 

