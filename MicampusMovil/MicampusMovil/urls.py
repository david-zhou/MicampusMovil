from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^(?P<Matricula>\w+)?\+?(?P<Password>\w+)?$','principal.views.v_LogIn'),
	url(r'^Principal/(?P<Matricula>\w+)?$','principal.views.v_index'),
	url(r'^Boleta/(?P<Matricula>\w+)??$','principal.views.v_Boleta'),
    url(r'^Practicas/(?P<Matricula>\w+)??$','principal.views.v_Practicas'),
    url(r'^Historial/(?P<Matricula>\w+)??$','principal.views.v_Historial_Academico'),
    url(r'^Servicio/(?P<Matricula>\w+)??$','principal.views.v_Servicio_Social_Inicio'),
    url(r'^Requisitos/(?P<Matricula>\w+)??$','principal.views.v_Servicio_Social_Requisitos'),
    url(r'^Contacto/(?P<Matricula>\w+)??$','principal.views.v_Servicio_Social_Contacto'),
    url(r'^Pasos/(?P<Matricula>\w+)??$','principal.views.v_Servicio_Social_Pasos'),
    url(r'^Programas/(?P<Matricula>\w+)??$','principal.views.v_Servicio_Social_Programas'),
    url(r'^Horario/(?P<Matricula>\w+)??$','principal.views.v_Horario'),
    url(r'^Titulacion/(?P<Matricula>\w+)??$','principal.views.v_Titulacion_Inicio'),
    url(r'^TRequisitos/(?P<Matricula>\w+)??$','principal.views.v_Titulacion_Requisitos'),
    url(r'^TActividades/(?P<Matricula>\w+)??$','principal.views.v_Titulacion_Actividades'),
    url(r'^TContacto/(?P<Matricula>\w+)??$','principal.views.v_Titulacion_Contacto'),

    # Examples:
    # url(r'^$', 'MicampusMovil.views.home', name='home'),
    # url(r'^MicampusMovil/', include('MicampusMovil.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
