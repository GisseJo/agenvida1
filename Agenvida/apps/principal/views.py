# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404 
from django.template import RequestContext
from django.core.mail import EmailMessage

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def dashboard(request):
    ideal_personal= request.user.profile.ideal_personal
    return render_to_response('index.html',{'ideal_personal':ideal_personal},context_instance=RequestContext(request))




def login_user(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/he')
    
    if request.POST:
        username = password = ''
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/he')
            else:
                    return render_to_response('login/noactivo.html', context_instance=RequestContext(request))
        else:
                return render_to_response('login/nousuario.html', context_instance=RequestContext(request))
    else:
        return render_to_response('login/login.html', context_instance=RequestContext(request))
 



def privado(request):
    usuario = request.user
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'    
    return render_to_response('login/privado.html',{'usuario':usuario,'ua':ua },context_instance=RequestContext(request))


def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')