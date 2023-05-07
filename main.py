import csv
import numpy as np

from clasealumnos import alumnos
from clasematerias import materias
from manejadroalumnos import manejadorAlumno
from manejadormaterias import manejadorMaterias

if __name__ == '__main__':
	alumnos=manejadorAlumno(9)
	materias=manejadorMaterias()
	alumnos.cargar()
	materias.cargar()
	print("""
1) Promedios de un alumno
2) Estudiantes que aprobaron una materia promocionando
3) Listado de alumnos
		""")
	opc=int(input(""))
	while opc!=0:
		match opc:
			case 1:
				dni=str(input("Ingrese DNI: "))
				while not alumnos.buscarAlumno(dni) and dni!="0":
					dni=str(input("Alumno no encontrado. Ingrese DNI: "))
				print("Promedio alumno (con y sin aplazos): ",materias.promediosAlumno(dni))
			case 2:
				mat=str(input("Ingrese el nombre de una materia")).lower()
				materias.promocionadosConMas7(mat,alumnos)
			case 3:
				alumnos.ordenar()
				alumnos.mostrarAlumnos()



		print("""
1) Promedios de un alumno
2) Estudiantes que aprobaron una materia promocionando
3) Listado de alumnos
			""")
		opc=int(input(""))
