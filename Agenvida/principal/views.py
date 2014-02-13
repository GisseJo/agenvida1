# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render_to_response, get_object_or_404,redirect 
from django.template import RequestContext
from django.core.mail import EmailMessage

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from principal.models import PropositoParticular, Proposito,Marcacion
##Pisa
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template import RequestContext
from django.template.loader import render_to_string


def generar_pdf(html):
    # Función para generar el archivo PDF y devolverlo mediante HttpResponse
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

@login_required(login_url='/login')
def libro_pdf(request, mes):
    # vista de ejemplo con un hipotético modelo Libro
    usuario = request.user
    prop_dios = Proposito.objects.filter(usuario=usuario, mes_ano__month=mes, vinculacion__id='1')
    prop_conmigo=Proposito.objects.filter(usuario=usuario, mes_ano__month=mes, vinculacion__id='2')
    prop_losdemas =Proposito.objects.filter(usuario=usuario, mes_ano__month=mes, vinculacion__id='3')
    prop_naturaleza=Proposito.objects.filter(usuario=usuario, mes_ano__month=mes, vinculacion__id='4')
    prop_particular=Proposito.objects.filter(usuario=usuario, mes_ano__month=mes, vinculacion__id='5')
    if not prop_dios.exists():
        prop_dios=None
    if not prop_conmigo.exists():
        prop_conmigo=None
    if not prop_losdemas.exists():
        prop_losdemas=None
    if not prop_naturaleza.exists():
        prop_naturaleza=None
    if not  prop_particular.exists():   
        prop_particular=None

        
    usuario = request.user
#   print request.user.profile.ideal_personal
        
    
    html = render_to_string('topdf.html',  {'pagesize':'A4', 'prop_dios':prop_dios, 'prop_losdemas':prop_losdemas, 'prop_conmigo':prop_conmigo, 'prop_naturaleza':prop_naturaleza, 'usuario':usuario,'prop_particular':prop_particular }, context_instance=RequestContext(request))
    return generar_pdf(html)



@login_required(login_url='/login')
def dashboard(request):
    ideal_personal= request.user.profile.ideal_personal
    nombre= request.user.first_name
    return render_to_response('index.html',{'ideal_personal':ideal_personal, 'nombre':nombre},context_instance=RequestContext(request))




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
 
def portada(request):
    if request.user.is_authenticated():
        return redirect('/he/')
    return render_to_response('nuevo.html', context_instance=RequestContext(request))
 
     


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