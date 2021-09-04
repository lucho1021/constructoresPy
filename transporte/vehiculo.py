class vehiculo:
    __nromotor = ""
    __nroruedas = 0
    __nroasientos = 0

    def __init__(self, nromotor, nroruedas, nroasientos):
        self.__nromotor = nromotor
        self.__nroruedas = nroasientos
        self.__nroasientos = nroasientos

    def getNromotor(self):
        return self.__nromotor

    def setNromotor(self, nromotor):
        self.__nromotor = nromotor
    
    def getNroruedas(self):
        return self.__nroruedas

    def setNroruedas(self, nroruedas):
        self.__nroruedas = nroruedas

    def getNroasientos(self):
        return self.__nroasientos

    def setNroasientos(self, nroasientos):
        self.__nroasientos = nroasientos

    def Arrancar(self):
        if self.__nroruedas >= 2:
            print("El vehiculo ha arrancado")
        else:
            print("El vehiculo no tiene las suficientes ruendas")

    def Acelerar(self):
        return "Acelerando el vehiculo"