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
		return render_to_response("Boleta.html" ,{"Matricula":Matricula,"NombreAlumno":NombreAlumno,"Alumnops":Alumnops}, context_instance = RequestContext(request))

def v_Practicas(request, Matricula):
	return render_to_response("Practicas.html", {"Matricula":Matricula}, context_instance = RequestContext(request))
	
def v_Servicio_Social(request, Matricula):
	return render_to_response("Servicio_Social.html", context_instance = RequestContext(request))


def v_Historial_Academico(request, Matricula):

	Historial = Materia.objects.raw("Select M.Clave_Materia, M.Nombre, GA.Calificacion_Final FROM (((principal_alumno AS A inner join principal_plan_de_estudios_materia AS PM ON A.Clave_Plan_De_Estudios_id = PM.Clave_Plan_De_Estudios_id )inner join principal_materia AS M ON M.Clave_Materia = PM.Clave_Materia_id) inner join principal_grupo AS G ON G.Clave_Materia_id = M.Clave_Materia   )left join principal_grupo_alumno AS GA ON GA.Clave_Grupo_id = G.Clave_Grupo WHERE A.Matricula = '"+Matricula+"' AND PM.Semestre = '1'")
	Segundo = Materia.objects.raw("Select M.Clave_Materia, M.Nombre, GA.Calificacion_Final FROM (((principal_alumno AS A inner join principal_plan_de_estudios_materia AS PM ON A.Clave_Plan_De_Estudios_id = PM.Clave_Plan_De_Estudios_id )inner join principal_materia AS M ON M.Clave_Materia = PM.Clave_Materia_id) inner join principal_grupo AS G ON G.Clave_Materia_id = M.Clave_Materia   )left join principal_grupo_alumno AS GA ON GA.Clave_Grupo_id = G.Clave_Grupo WHERE A.Matricula = '"+Matricula+"' AND PM.Semestre = '2'")
	Tercero = Materia.objects.raw("Select M.Clave_Materia, M.Nombre, GA.Calificacion_Final FROM (((principal_alumno AS A inner join principal_plan_de_estudios_materia AS PM ON A.Clave_Plan_De_Estudios_id = PM.Clave_Plan_De_Estudios_id )inner join principal_materia AS M ON M.Clave_Materia = PM.Clave_Materia_id) inner join principal_grupo AS G ON G.Clave_Materia_id = M.Clave_Materia   )left join principal_grupo_alumno AS GA ON GA.Clave_Grupo_id = G.Clave_Grupo WHERE A.Matricula = '"+Matricula+"' AND PM.Semestre = '3'")
	Cuarto = Materia.objects.raw("Select M.Clave_Materia, M.Nombre, GA.Calificacion_Final FROM (((principal_alumno AS A inner join principal_plan_de_estudios_materia AS PM ON A.Clave_Plan_De_Estudios_id = PM.Clave_Plan_De_Estudios_id )inner join principal_materia AS M ON M.Clave_Materia = PM.Clave_Materia_id) inner join principal_grupo AS G ON G.Clave_Materia_id = M.Clave_Materia   )left join principal_grupo_alumno AS GA ON GA.Clave_Grupo_id = G.Clave_Grupo WHERE A.Matricula = '"+Matricula+"' AND PM.Semestre = '4'")
	Quinto = Materia.objects.raw("Select M.Clave_Materia, M.Nombre, GA.Calificacion_Final FROM (((principal_alumno AS A inner join principal_plan_de_estudios_materia AS PM ON A.Clave_Plan_De_Estudios_id = PM.Clave_Plan_De_Estudios_id )inner join principal_materia AS M ON M.Clave_Materia = PM.Clave_Materia_id) inner join principal_grupo AS G ON G.Clave_Materia_id = M.Clave_Materia   )left join principal_grupo_alumno AS GA ON GA.Clave_Grupo_id = G.Clave_Grupo WHERE A.Matricula = '"+Matricula+"' AND PM.Semestre = '5'")
	Sexto = Materia.objects.raw("Select M.Clave_Materia, M.Nombre, GA.Calificacion_Final FROM (((principal_alumno AS A inner join principal_plan_de_estudios_materia AS PM ON A.Clave_Plan_De_Estudios_id = PM.Clave_Plan_De_Estudios_id )inner join principal_materia AS M ON M.Clave_Materia = PM.Clave_Materia_id) inner join principal_grupo AS G ON G.Clave_Materia_id = M.Clave_Materia   )left join principal_grupo_alumno AS GA ON GA.Clave_Grupo_id = G.Clave_Grupo WHERE A.Matricula = '"+Matricula+"' AND PM.Semestre = '6'")
	Septimo = Materia.objects.raw("Select M.Clave_Materia, M.Nombre, GA.Calificacion_Final FROM (((principal_alumno AS A inner join principal_plan_de_estudios_materia AS PM ON A.Clave_Plan_De_Estudios_id = PM.Clave_Plan_De_Estudios_id )inner join principal_materia AS M ON M.Clave_Materia = PM.Clave_Materia_id) inner join principal_grupo AS G ON G.Clave_Materia_id = M.Clave_Materia   )left join principal_grupo_alumno AS GA ON GA.Clave_Grupo_id = G.Clave_Grupo WHERE A.Matricula = '"+Matricula+"' AND PM.Semestre = '7'")
	Octavo = Materia.objects.raw("Select M.Clave_Materia, M.Nombre, GA.Calificacion_Final FROM (((principal_alumno AS A inner join principal_plan_de_estudios_materia AS PM ON A.Clave_Plan_De_Estudios_id = PM.Clave_Plan_De_Estudios_id )inner join principal_materia AS M ON M.Clave_Materia = PM.Clave_Materia_id) inner join principal_grupo AS G ON G.Clave_Materia_id = M.Clave_Materia   )left join principal_grupo_alumno AS GA ON GA.Clave_Grupo_id = G.Clave_Grupo WHERE A.Matricula = '"+Matricula+"' AND PM.Semestre = '8'")
	A = Alumno.objects.raw("Select * FROM principal_alumno AS A WHERE A.Matricula = '"+Matricula+"'")
	
	return render_to_response("Historial_Academico.html" ,{"Matricula":Matricula,"Historial":Historial, "Segundo":Segundo, "Tercero":Tercero,"Cuarto":Cuarto,"Quinto":Quinto,"Sexto":Sexto,"Septimo":Septimo,"Octavo":Octavo, "A":A}, context_instance = RequestContext(request))


def v_Servicio_Social_Requisitos(request, Matricula):
	return render_to_response("Servicio_Social_Requisitos.html",{"Matricula":Matricula}, context_instance = RequestContext(request))

def v_Servicio_Social_Inicio(request, Matricula):
	return render_to_response("Servicio_Social_Inicio.html",{"Matricula":Matricula}, context_instance = RequestContext(request))

def v_Servicio_Social_Contacto(request, Matricula):
	return render_to_response("Servicio_Social_Contacto.html",{"Matricula":Matricula}, context_instance = RequestContext(request))

def v_Servicio_Social_Pasos(request, Matricula):
	return render_to_response("Servicio_Social_Pasos.html",{"Matricula":Matricula}, context_instance = RequestContext(request))

def v_Servicio_Social_Programas(request, Matricula):
	return render_to_response("Servicio_Social_Programas.html",{"Matricula":Matricula}, context_instance = RequestContext(request))

def v_Horario(request, Matricula):

	horario = Materia.objects.raw("Select * FROM (principal_grupo AS G INNER JOIN principal_grupo_alumno AS GA ON GA.Clave_Grupo_id = G.Clave_Grupo) INNER JOIN principal_materia AS M ON M.Clave_Materia = G.Clave_Materia_id WHERE GA.Matricula_id = '"+Matricula+"' AND G.Ciclo_Escolar = 'cualquier cosa'")
	return render_to_response("Horario.html",{"Matricula":Matricula, "horario":horario}, context_instance = RequestContext(request))

def v_Titulacion_Inicio(request, Matricula):
	return render_to_response("Titulacion_Inicio.html",{"Matricula":Matricula}, context_instance = RequestContext(request))

def v_Titulacion_Requisitos(request, Matricula):
	return render_to_response("Titulacion_Requisitos.html",{"Matricula":Matricula}, context_instance = RequestContext(request))

def v_Titulacion_Actividades(request, Matricula):
	return render_to_response("Titulacion_Actividades.html",{"Matricula":Matricula}, context_instance = RequestContext(request))

def v_Titulacion_Contacto(request, Matricula):
	return render_to_response("Titulacion_Contacto.html",{"Matricula":Matricula}, context_instance = RequestContext(request))