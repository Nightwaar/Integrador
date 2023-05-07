class materias:
    __dni=''
    __nombremateria=''
    __fecha=''
    __nota=''
    __aprobacion=''
    def __init__(self,dni,nombre,fecha,nota,aprobacion):
        self.__dni=dni
        self.__nombremateria=nombre
        self.__fecha=fecha
        self.__nota=nota
        self.__aprobacion=aprobacion
    def __str__(self):
        return f"{self.__dni} {self.__nombremateria} {self.__fecha} {self.__nota} {self.__aprobacion}"
    def getdni(self):
        return self.__dni
    def fecha(self):
        return self.__fecha
    def getnota(self):
        return self.__nota
    def getnombremateria(self):
        return self.__nombremateria
    def getaprobacion(self):
        return self.__aprobacion
    def verifMateria(self,materia):
        flag=False
        if materia==self.__nombremateria:
            flag=True
            