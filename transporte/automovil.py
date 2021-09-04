from transporte.vehiculo import vehiculo
class automovil(vehiculo):
    __guantera = True
    __nropuertas = 0
    
    def __init__(self, nromotor, nroruedas, nroasientos, guantera, nropuertas):
        vehiculo.__init__(self, nromotor, nroruedas, nroasientos)

        self.__guantera = guantera
        self.__nropuertas = nropuertas

    def getGuantera(self):
        return self.__guantera

    def setGuantera(self, guantera):
        self.__guantera = guantera

    def getNropuertas(self):
        return self.__nropuertas

    def setNropuertas(self, nropuertas):
        self.__nropuertas = nropuertas

    def reservar(self):
        return "Vehiculo en reversa"