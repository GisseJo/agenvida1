# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404 
from django.core.context_processors import csrf
from forms  import UserProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance= request.user.profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/loggedin')
	else:
		user= request.user
		profile = user.profile
		form = UserProfileForm(instance=profile)
		args = ()
		args.update(csrf(request))
		agrs['form']= form
		return render_to_response('userprofile/profile.html', args)


