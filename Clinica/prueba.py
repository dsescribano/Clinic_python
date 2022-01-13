from datetime import datetime, timedelta


# Clase que sirve como herencia para las clases que representan a los distintos tipos de pruebas
class Prueba:
    def __init__(self, nombrePaciente, nombreEnfermero, nombreTecnico):
        self.__nombrePaciente = nombrePaciente
        self.__nombreEnfermero = nombreEnfermero
        self.__nombreTecnico = nombreTecnico
        self.__nombrePrueba = ""
        self.__fechaPrueba = datetime.now()
        self.__procesada = False
        self.__positivo = False

 # Métodos

    def getFechaPrueba(self):
        return self.__fechaPrueba

    def addNombrePrueba(self, nombrePrueba):
        self.__nombrePrueba = nombrePrueba.lower()

    def getNombrePrueba(self):
        return self.__nombrePrueba.lower()

    def getNombrePaciente(self):
        return self.__nombrePaciente.lower()

    def getNombreEnfermero(self):
        return self.__nombreEnfermero.lower()

    def getNombreTecnico(self):
        return self.__nombreTecnico.lower()

    def setPositivo(self, positivo):
        self.__positivo = positivo

    def getPositivo(self):
        if self.__positivo:
            return "si"
        else:
            return "no"

    def setProcesada(self, procesada):
        self.__procesada = procesada

    def getProcesada(self):
        if self.__procesada:
            return "si"
        else:
            return "no"


# Clase para instanciar pruebas pcr
class PCR(Prueba):
    def __init__(self, nombrePaciente, nombreEnfermero, nombreTecnico):
        super().__init__(nombrePaciente, nombreEnfermero, nombreTecnico)
        self.__fechaValidez = str(self.getFechaPrueba() + timedelta(days=15))
        self.addNombrePrueba("pcr")

 # Métodos

    def getFechaValidez(self):
        return self.__fechaValidez


# Clase para instanciar pruebas de antigenos
class Antigenos(Prueba):
    def __init__(self, nombrePaciente, nombreEnfermero, nombreTecnico):
        super().__init__(nombrePaciente, nombreEnfermero, nombreTecnico)
        self.addNombrePrueba("antigenos")


# Clase para instanciar pruebas serologicas
class Serologico(Prueba):
    def __init__(self, nombrePaciente, nombreEnfermero, nombreTecnico):
        super().__init__(nombrePaciente, nombreEnfermero, nombreTecnico)
        anticuerpos = 0
        self.__fechaValidez = str(self.getFechaPrueba() + timedelta(days=183))
        self.addNombrePrueba("serologico")

 # Métodos
    def getFechaValidez(self):
        return self.__fechaValidez

    def setAnticuerpos(self, anticuerpos):
        if 0 <= anticuerpos <= 10:
            self.__anticuerpos = anticuerpos

            if anticuerpos > 2:
                self.setPositivo(True)
            else:
                self.setPositivo(False)

        else:
            print("El valor introducido no es correcto")

    def getAnticuerpos(self):
        return self.__anticuerpos

    def getInmunidad(self):
        if self.__anticuerpos > 2:
            return "si"
        else:
            return "no"
