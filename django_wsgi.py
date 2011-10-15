import os, sys
import django.core.handlers.wsgi

sys.path.insert(0, '/export/web/intersys.mx')
sys.path.insert(0, '/export/web/intersys.mx/intersys')

os.environ['PROJECT_DIR'] = '/export/web/intersys.mx/intersys'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

os.environ['PYTHON_EGG_CACHE'] = '/tmp'
application = django.core.handlers.wsgi.WSGIHandler()
