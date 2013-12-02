from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from principal.models import Alumno
from principal.models import Grupo_Alumno
from principal.models import Materia
from principal.models import Grupo

def v_index(request,Matricula):
	return render_to_response("index.html", {"Matricula":Matricula}, context_instance = RequestContext(request))

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
		NombreAlumno = Alumno.objects.raw("Select M.Nombre, GA.Clave_Grupo_Alumno, A.Matricula, A.Nombre as NombreAlumno, GA.C1 as Cal1, GA.C2 as Cal2, GA.C3 as Cal3, GA.Faltas_Totales as Faltas, GA.Calificacion_Final as Califinal FROM (principal_grupo_alumno GA INNER JOIN principal_alumno A ON  GA.Matricula_id = A.Matricula ) INNER JOIN principal_grupo G ON GA.Clave_Grupo_id = G.Clave_Grupo INNER JOIN principal_materia  M ON G.Clave_Materia_id = M.Clave_Materia WHERE Matricula = '"+Matricula+"'") 
		Alumnops = Alumno.objects.raw("Select A.Nombre, A.Matricula FROM principal_alumno A WHERE (A.Matricula ='"+Matricula+"')") 
		#Boleta = Alumno.objects.raw("Select A.Nombre as NombreAlumno, A.Matricula, GA.Clave_Grupo_Alumno, M.Clave_Materia, G.Clave_Grupo, M.Nombre as NombreMateria, GA.C1 as Cal1, GA.C2 as Cal2, GA.C3 as Cal3, GA.Faltas_Totales as Faltas, GA.Calificacion_Final as Califinal FROM (principal_grupo_alumno GA INNER JOIN principal_alumno A ON GA.Matricula_id = A.Matricula) INNER JOIN (principal_materia M INNER JOIN principal_grupo G ON G.Clave_Materia_id=M.Clave_Materia) ON G.Clave_Grupo=GA.Clave_Grupo_id WHERE (A.Matricula ='"+str(Matricula)+"'")
		return render_to_response("Boleta.html" ,{"NombreAlumno":NombreAlumno,"Alumnops":Alumnops}, context_instance = RequestContext(request))

def v_Practicas(request, Matricula):
	return render_to_response("Practicas.html", {"Matricula":Matricula}, context_instance = RequestContext(request))