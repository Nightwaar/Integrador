import csv
import numpy as np
from clasealumnos import alumnos
class manejadorAlumno():
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self, dimension, incremento=5):
        self.__alumnos = np.empty(dimension, dtype=alumnos)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento=incremento
    def agregarAlumno(self, unAlumno):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__alumnos.resize(self.__dimension)
        self.__alumnos[self.__cantidad]=unAlumno
        self.__cantidad += 1
    def getAlumno(self, indice):
        return self.__alumnos[indice]
    def mostrarAlumnos(self):
        for i in range(self.__cantidad):
            self.__alumnos[i].mostrarDatosAlumno()
    def cargar(self,):
        archivo=open("alumnos.csv")
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.__agregarAlumno(alumnos(fila[0],fila[1],fila[2],fila[3],fila[4]))
    def buscaralumno(self,dni):
        flag=False
        i=0
        while not flag and i<self.__cantidad:
            flag=self.__alumnos[i].verificarDni(dni)
            i+=1
        if flag:
            i-=1
        else:
            i=False
        return i
    def ordenaraño(self):
        cont=0
        ordenado=False
        tamaño=self.__cantidad
        comparaciones=tamaño
        for i in range(0,tamaño):
            if ordenado==True:
                break
            for j in range(0,comparaciones-1):
                ordenado=True
                cont+=1
                if self.__alumnos[j].getaño()>self.__alumnos[j+1].getaño():
                    ordenado=False
                    aux=self.__alumnos[j]
                    self.__alumnos[j]=self.__alumnos[j+1]
                    self.__alumnos[j+1]=aux
                comparaciones-=1
            return
    def ordenarnombre(self):
        cont=0
        ordenado=False
        tamaño=self.__cantidad
        comparaciones=tamaño
        for i in range(0,tamaño):
            if ordenado==True:
                break
            for j in range(0,comparaciones-1):
                ordenado=True
                cont+=1
                if self.__alumnos[j].getnombre()>self.__alumnos[j+1].getnombre():
                    ordenado=False
                    aux=self.__alumnos[j]
                    self.__alumnos[j]=self.__alumnos[j+1]
                    self.__alumnos[j+1]=aux
                comparaciones-=1
            return
    def ordenar(self):
        self.__ordenaraño()
        self.__ordenarnombre()