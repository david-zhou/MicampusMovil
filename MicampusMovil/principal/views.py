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

def v_Boleta(request, Matricula):
		Boleta = Clientes.objects.raw("Select A.Nombre as NombreAlumno, A.Matricula, M.Nombre as NombreMateria, GA.C1, GA.C2, GA.C3, GA.Faltas_Totales, GA.Calificacion_Final FROM principal_grupo_alumno GA, principal_alumno A, principal_materia M, principal_grupo G WHERE (A.Matricula = '"'%%%%'+str(Matricula)+'%%%%'"'  ) AND M.Clave_Materia=G.Clave_Materia_id AND GA.Matricula_id = A.Matricula")
		return render_to_response("Boleta.html" ,{"MateriaBoleta":Boleta}, context_instance = RequestContext(request))