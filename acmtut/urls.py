from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'encuestas.views.inicio', name='inicio'),
    url(r'^activas$', 'encuestas.views.activas', name='activas'),
    url(r'^votar/(\d)/(\d)$', 'encuestas.views.realizar_voto'),
    url(r'^votacion/(\d)$', 'encuestas.views.votacion'),
    url(r'^nueva_votacion/$', 'encuestas.views.nueva_votacion'),

    # url(r'^acmtut/', include('acmtut.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
