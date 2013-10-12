from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from principal.resource import MarcacionResource, VinculacionResource,PropositoResource,PParticularResource
from django.views.generic.simple import direct_to_template

admin.autodiscover()

marcacion_resource = MarcacionResource()
vinculacion_resource = VinculacionResource()
proposito_resource = PropositoResource()
pparticular_resource = PParticularResource()


from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','principal.views.portada'),
    (r'^login/$', 'principal.views.login_user'),
   (r'^he/','principal.views.dashboard' ),
    (r'^privado/','principal.views.dashboard' ),
   (r'^cerrar/$','principal.views.cerrar'),
    (r'^api/', include(marcacion_resource.urls)),
    (r'^api/', include(vinculacion_resource.urls)),
    (r'^api/', include(proposito_resource.urls)),
    (r'^api/', include(pparticular_resource.urls)),  
   # (r'^accounts/', include('registration.urls')),
     (r'^accounts/', include('allauth.urls')), 
      url(r'^accounts/', include('userprofile.urls')),
    (r'^/accounts/sugerencias/', direct_to_template, {'template': 'sugerencias.html'}),
    (r'^hep/', direct_to_template, {'template': 'hep.html'}),
    (r'^about/', direct_to_template, {'template': 'about.html'}),
    (r'^contacto/', direct_to_template, {'template': 'contacto.html'}),
    
)