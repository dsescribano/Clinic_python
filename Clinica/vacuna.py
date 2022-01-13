from datetime import date, timedelta


# Clase que sirve como herencia para las clases que representan a las distintos tipos de vacunas
class Vacuna:

 # Constructor
    def __init__(self, nombrePaciente, nombreEnfermero):
        self.__nombrePaciente = nombrePaciente
        self.__nombreEnfermero = nombreEnfermero
        self.__nombreVacuna = ""
        self.__fechaVacuna = date.today()

 # Métodos

    def setNombreVacuna(self, nombreVacuna):
        self.__nombreVacuna = nombreVacuna

    def getNombreVacuna(self):
        return self.__nombreVacuna.lower()

    def getNombrePaciente(self):
        return self.__nombrePaciente.lower()

    def getFechaVacuna(self):
        return str(self.__fechaVacuna)

    def getNombreEnfermero(self):
        return self.__nombreEnfermero.lower()


# Clase para instanciar vacunas de la clase Johnson & Johnson
class JohnsonAndJohnson(Vacuna):
    def __init__(self, nombrePaciente, nombreEnfermero):
        super().__init__(nombrePaciente, nombreEnfermero)
        self.setNombreVacuna("Johnson & Johnson")


# Clase para instanciar vacunas de la clase Pfizer
class Pfizer(Vacuna):
    def __init__(self, nombrePaciente, nombreEnfermero):
        super().__init__(nombrePaciente, nombreEnfermero)
        self.setNombreVacuna("Pfizer")


# Clase para instanciar vacunas de la clase Moderna
class Moderna(Vacuna):
    def __init__(self, nombrePaciente, nombreEnfermero):
        super().__init__(nombrePaciente, nombreEnfermero)
        self.setNombreVacuna("Moderna")
