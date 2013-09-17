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


def inicio(request):
    
    return render_to_response('index.html',context_instance=RequestContext(request))