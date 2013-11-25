from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^(?P<Matricula>\w+)?\+?(?P<Password>\w+)?$','principal.views.v_LogIn'),
	url(r'^Principal/(?P<Matricula>\w+)?$','principal.views.v_index'),
	url(r'^Boleta/$','principal.views.v_Boleta'),
    # Examples:
    # url(r'^$', 'MicampusMovil.views.home', name='home'),
    # url(r'^MicampusMovil/', include('MicampusMovil.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
