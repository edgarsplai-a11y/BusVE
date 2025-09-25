class bus:
    def __init__(self, plaza_maxima, matricula):
        self.__plaza_maxima = plaza_maxima
        self.__matricula = matricula

    def Getplaza_maxima(self):
        return self.__plaza_maxima
    
    def Getmatricula(self):
        return self.__matricula