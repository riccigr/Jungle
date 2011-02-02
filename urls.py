from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^jungle/', include('jungle.foo.urls')),
    #(r'^$', 'agenda.views.index'),
     (r'^$', 'agenda.views.lista'),
     (r'^adiciona/$', 'agenda.views.adiciona'),
     (r'^item/(?P<nr_item>\d+)/$','agenda.views.item'),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
)
