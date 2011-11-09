from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'intersys.views.home', name='home'),
    (r'^$', 'home.views.index'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
	'document_root': settings.MEDIA_ROOT,
    }),
    # url(r'^intersys/', include('intersys.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /admin", mimetype="text/plain")),
)
urlpatterns += staticfiles_urlpatterns()
