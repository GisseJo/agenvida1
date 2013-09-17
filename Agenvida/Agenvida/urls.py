from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from principal.resource import MarcacionResource, VinculacionResource,PropositoResource

admin.autodiscover()

marcacion_resource = MarcacionResource()
vinculacion_resource = VinculacionResource()
proposito_resource = PropositoResource()


from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','principal.views.inicio'),
    (r'^api/', include(marcacion_resource.urls)),
    (r'^api/', include(vinculacion_resource.urls)),
    (r'^api/', include(proposito_resource.urls)),   

    
)
