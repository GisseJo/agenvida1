"""
WSGI config for Agenvida project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys
 
sys.path.append('/usr/lib64/python2.6')
sys.path.append('/usr/lib/python2.6/site-packages/django')
 
sys.path.append('/var/www/agenvida.com/Agenvida')
sys.path.append('/var/www/agenvida.com/Agenvida/Agenvida')
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Agenvida.settings")
 
 
# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
 
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
 
from django.core.handlers.wsgi import WSGIHandler
 
application = WSGIHandler()