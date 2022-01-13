import persona
import vacuna

# Clase para generar la base de datos


class BaseDatos:
    def __init__(self):
        # Listas de personas
        self.__pacientes = []
        self.__enfermeros = []
        self.__tecnicos = []

        # Listas de pruebas
        self.__PCRsRealizadas = {}
        self.__antigenosRealizadas = {}
        self.__serologicasRealizadas = {}

        # Listas de vacunas
        self.__vacunasAdministradas = []

 # Métodos para obtener listas de personas
    def getPacientes(self):
        return self.__pacientes

    def getEnfermeros(self):
        return self.__enfermeros

    def getTecnicos(self):
        return self.__tecnicos

 # Métodos para añadir o quitar personas
    def addPersona(self, persona, lista):
        lista.append(persona)

    def deletePersona(self, nombre, lista):
        # Comprueba si la lista está vacía
        if lista:
            nombreExiste = False

            # Comprueba si el nombre introducido está en la lista
            for persona in lista:
                if persona.getNombre() == nombre:
                    nombreExiste = True

            # Si el nombre no existe
            if not nombreExiste:
                print("El nombre introducido no se encuentra en la lista")
            # si el nombre existe lo borra
            else:
                for persona in lista:
                    if persona.getNombre() == nombre:
                        lista.remove(persona)
                        break
        else:
            print("La lista a la que se quiere acceder está vacía")

 # Métodos para buscar personas en la base de datos

    def buscarEnfermero(self, nombre):
        for enfermero in self.__enfermeros:
            if enfermero.getNombre() == nombre.lower():
                return enfermero
                break

    def buscarTecnico(self, nombre):
        for tecnico in self.__tecnicos:
            if tecnico.getNombre() == nombre.lower():
                return tecnico
                break

    def buscarPaciente(self, nombre):
        for paciente in self.__pacientes:
            if paciente.getNombre() == nombre.lower():
                return paciente
                break

    # Comprueba si existe una persona en la lista añadida como parámetro
    def existePersona(self, nombre, lista):
        personaEncontrada = False
        for persona in lista:
            if persona.getNombre() == nombre.lower():
                personaEncontrada = True
                break
        return personaEncontrada

    # Crea una lista con los pacientes asociados a un sanitario
    def listaPacienteXSanitario(self, nombreSanitario, tipoSanitario):
        lista = []
        # Comprueba si el tipo de sanitario es enfermero o tecnico
        if tipoSanitario.lower() == "enfermero" or tipoSanitario.lower() == "enfermera":
            for paciente in self.__pacientes:
                # Comprueba si el nombre del sanitario asociado al paciente coincide con el introducido como parámetro
                if paciente.getEnfermeroVacuna() == nombreSanitario.lower() or paciente.getEnfermeroPrueba() == nombreSanitario.lower():
                    lista.append(paciente)
        elif tipoSanitario.lower() == "tecnico":
            for paciente in self.__pacientes:
                # Comprueba si el nombre del sanitario asociado al paciente coincide con el introducido como parámetro
                if paciente.getTecnicoAsignado() == nombreSanitario.lower():
                    lista.append(paciente)
        else:
            print("El tipo de sanitario introducido no es correcto.")
        return lista

    # Imprime en pantalla una lista con datos de los pacientes asociados a un sanitario
    def printListaXSanitario(self, nombreSanitario, tipoSanitario):

        # Comprueba el tipo de sanitario introducido
        if tipoSanitario.lower() == "enfermero":

            # Analiza si existe el enfermero introducido como parámetro
            if self.existePersona(nombreSanitario, self.getEnfermeros()):
                for paciente in self.listaPacienteXSanitario(nombreSanitario, tipoSanitario):

                    # Imprime los datos de los pacientes añadidos a la lista
                    print(f"Nombre: {paciente.getNombre()}. Fecha cita prueba: {paciente.getFechaCitaPrueba()}. Prueba solicitada: {paciente.getPruebaSolicitada()}. Fecha cita vacunacion: {paciente.getFechaCitaVacuna()}. Vacuna asignada: {paciente.getVacunaAsignada()}. Fecha final cuarentena: {paciente.getFinCuarentena()}. Vacunas administradas: {paciente.getVacunas()}. Inmunizado: {paciente.getInmunizacion()}")

            else:
                print("Los datos del sanitario introducidos no son correctos")

        # Cuando el tipo de sanitario es un tecnico
        elif tipoSanitario.lower() == "tecnico":
            if self.existePersona(nombreSanitario, self.getTecnicos()):
                for paciente in self.listaPacienteXSanitario(nombreSanitario, tipoSanitario):
                    print(f"Nombre: {paciente.getNombre()}. Fecha cita prueba: {paciente.getFechaCitaPrueba()}. Prueba solicitada: {paciente.getPruebaSolicitada()}. Fecha cita vacunacion: {paciente.getFechaCitaVacuna()}. Vacuna asignada: {paciente.getVacunaAsignada()}. Fecha final cuarentena: {paciente.getFinCuarentena()}. Vacunas administradas: {paciente.getVacunas()}. Inmunizado: {paciente.getInmunizacion()}")
            else:
                print("Los datos del sanitario introducidos no son correctos")
        else:
            print("El tipo de sanitario introducido no es correcto")

 # Métodos para añadir pruebas a las listas correspondientes

    def addPruebaSerologica(self, serologico):
        key = len(self.__serologicasRealizadas)
        self.__serologicasRealizadas[key] = serologico

    def addPruebaPCR(self, pcr):
        key = len(self.__PCRsRealizadas)
        self.__PCRsRealizadas[key] = pcr

    def addPruebaAntigenos(self, antigenos):
        key = len(self.__antigenosRealizadas)
        self.__antigenosRealizadas[key] = antigenos

    def getPruebasRealizadas(self, prueba):
        if prueba.lower() == "pcr":
            return self.__PCRsRealizadas
        elif prueba.lower() == "antigenos":
            return self.__antigenosRealizadas
        elif prueba.lower() == "serologico":
            return self.__serologicasRealizadas

 # Métodos para obtener una prueba concreta utilizando la key del diccionario

    def getPCR(self, key):
        return self.__PCRsRealizadas.get(key)

    def getAntigeno(self, key):
        return self.__antigenosRealizadas.get(key)

    def getSerologico(self, key):
        return self.__serologicasRealizadas.get(key)

 # Métodos para interactuar con la lista de vacunas

    def setVacuna(self, nombreVacuna, nombrePaciente, nombreEnfermero):
        if nombreVacuna.lower() == "johnson & johnson":
            self.__vacunasAdministradas.append(
                vacuna.JohnsonAndJohnson(nombrePaciente, nombreEnfermero))
        elif nombreVacuna.lower() == "moderna":
            self.__vacunasAdministradas.append(
                vacuna.Moderna(nombrePaciente, nombreEnfermero))
        elif nombreVacuna.lower() == "pfizer":
            self.__vacunasAdministradas.append(
                vacuna.Pfizer(nombrePaciente, nombreEnfermero))
        else:
            return "El nombre de la vacuna introducido no es correcto"

    def getVacunasAdministradas(self):
        return self.__vacunasAdministradas
