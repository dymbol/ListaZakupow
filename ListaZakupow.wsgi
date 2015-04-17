import os
import sys
sys.path.append('/opt/ListaZakupow/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ListaZakupow.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
 
