from django.db import models

class Plan_De_Estudios(models.Model):
	Clave_Plan_De_Estudios = models.CharField(primary_key = True, max_length = 10)
	Nombre = models.CharField(max_length = 50)

class Escuela(models.Model):
	Clave_Escuela = models.CharField(primary_key = True, max_length = 4)
	Nombre_completo = models.CharField(max_length = 50)

class Carrera(models.Model):
	Clave_Carrera = models.CharField(primary_key = True, max_length = 4)
	Nombre = models.CharField(max_length = 50)
	Clave_Escuela = models.ForeignKey(Escuela)

class Alumno(models.Model):
	Matricula = models.CharField(primary_key = True, max_length = 6)
	Nombre = models.CharField(max_length = 50)
	Clave_Carrera = models.ForeignKey(Carrera)
	Clave_Plan_De_Estudios = models.ForeignKey(Plan_De_Estudios)
	Concentracion = models.CharField(max_length = 20)
	Contrasenia = models.CharField(max_length = 10)


class Materia(models.Model):
	Clave_Materia = models.CharField(primary_key = True, max_length = 5)
	Nombre = models.CharField(max_length = 50)

class Grupo(models.Model):
	Clave_Grupo = models.CharField(primary_key = True, max_length = 5)
	Profesor = models.CharField(max_length = 40)
	Salon = models.CharField(max_length = 20)
	Horario = models.CharField(max_length = 40)
	Clave_Materia = models.ForeignKey(Materia)
	Tipo = models.CharField(max_length = 2)
	Ciclo_Escolar = models.CharField(max_length = 25)

class Grupo_Alumno(models.Model):
	Clave_Grupo_Alumno = models.AutoField(primary_key = True)
	Clave_Grupo = models.ForeignKey(Grupo)
	Matricula = models.ForeignKey(Alumno)
	C1 = models.IntegerField()
	C2 = models.IntegerField()
	C3 = models.IntegerField()
	Calificacion_Final = models.IntegerField()
	Faltas_Totales = models.IntegerField()
	Fecha_Calificacion_Final = models.DateTimeField()
	
	class Meta:
		unique_together = ('Clave_Grupo','Matricula')	

class Plan_De_Estudios_Materia(models.Model):
	Clave_Plan_De_estudios_Materia = models.AutoField(primary_key = True)
	Clave_Plan_De_Estudios = models.ForeignKey(Plan_De_Estudios)
	Clave_Materia = models.ForeignKey(Materia)
	Semestre = models.IntegerField()
	
	class Meta:
		unique_together = ('Clave_Plan_De_Estudios','Clave_Materia')