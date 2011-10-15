import os, sys
import django.core.handlers.wsgi

sys.path.insert(0, '/export/web/intersys')
sys.path.insert(0, '/export/web/intersys/intersys')

os.environ['PROJECT_DIR'] = '/export/web/intersys/intersys'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

os.environ['PYTHON_EGG_CACHE'] = '/tmp'
application = django.core.handlers.wsgi.WSGIHandler()
