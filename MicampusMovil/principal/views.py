from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from principal.models import Alumno

def v_index(request,Matricula):
	return render_to_response("index.html" , context_instance = RequestContext(request))

def v_LogIn(request,Matricula,Password):
	try:	
		vato = Alumno.objects.get(pk = Matricula)
		if(vato.Contrasenia == Password):
			return HttpResponseRedirect("/Principal/"+Matricula)
		else:
			Negativo = 1
			return render_to_response("LogIn.html" ,{"Negativo":Negativo}, context_instance = RequestContext(request))
	except:
		if Matricula is None:
			Negativo = 0
		else:
			Negativo = 1
		return render_to_response("LogIn.html" ,{"Negativo":Negativo}, context_instance = RequestContext(request))

