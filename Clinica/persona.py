from datetime import date, timedelta
import base_datos
import prueba
import vacuna

# __Clase que sirve como herencia para representar a las distintas personas que se almacenan y hacen uso del programa__


class Persona:

    # Constructor
    def __init__(self, nombre, apellido1, apellido2):
        self.__nombre = f"{apellido1} {apellido2}, {nombre}"

    # Devuelve el valor del campo nombre
    def getNombre(self):
        return self.__nombre.lower()

    # Modifica el valor del campo nombre
    def setNombre(self, nombre, apellido1, apellido2):
        self.__nombre = f"{apellido1} {apellido2}, {nombre}"


# __Clase para instanciar pacientes__
class Paciente(Persona):

    def __init__(self, nombre, apellido1, apellido2):
        super().__init__(nombre, apellido1, apellido2)
        self.__contagiado = False
        self.__vacuna = ["", ""]
        self.__pruebaSolicitada = ""
        self.__vacunaAsignada = ""
        self.__enfermeroPrueba = ""
        self.__enfermeroVacuna = ""
        self.__tecnicoAsignado = ""
        self.__fechaFinCuarentena = ""
        self.__fechaCitaPrueba = ""
        self.__fechaCitaVacuna = ""
        self.__fechaFinInmunidad = ""

 # Métodos relacionados con la inmunidad del paciente

    # Devuelve la fecha en la que acaba la caurentena
    def getFinCuarentena(self):
        return self.__fechaFinCuarentena

    # Establece la fecha en la que acaba la inmuniad
    def setFechaInmunidad(self):
        self.__fechaFinInmunidad = date.today() + timedelta(days=183)

    # Devuelve si el paciente está inmunizado o no
    def getInmunizacion(self):
        if self.__fechaFinInmunidad != "":
            if self.__fechaFinInmunidad > date.today():
                return "Si"
            else:
                return "No"
        else:
            return "No"

 # Métodos relacionados con el estado de contagio del paciente

    # Devuelve si el paciente está contagiado o no
    def getPacienteContagiado(self):
        if self.__fechaFinCuarentena != "":
            if self.__fechaFinCuarentena > date.today():
                self.__contagiado = True
            else:
                self.__contagiado = False
        return self.__contagiado

    # Establece si el paciente está contagiado o no
    def setPacienteContagiado(self):
        self.__contagiado = True
        self.__fechaFinCuarentena = date.today() + timedelta(days=10)

 # Métodos relacionados con la vacunación del paciente

    # Comprueba las dosis administradas
    def __getDosisVacuna(self):
        dosis = 0
        for number in range(2):
            if self.__vacuna[number] != "":
                dosis += 1
        return dosis

    # Establece la fecha de la cita para vacunarse
    def setFechaCitaVacuna(self, year, month, dayOfMonth):
        self.__fechaCitaVacuna = date(year, month, dayOfMonth)
        return self.__fechaCitaVacuna

    # Devuelve la fecha de la cita para la vacunación
    def getFechaCitaVacuna(self):
        return self.__fechaCitaVacuna

    # Elimina todos los datos acerca de la vacunación
    def deleteVacunaAsignada(self):
        self.__fechaCitaVacuna = ""
        self.__vacunaAsignada = ""
        self.__enfermeroVacuna = ""

    # Devuelve el nombre de la vacuna asignada
    def getVacunaAsignada(self):
        return self.__vacunaAsignada

    # Establce el nombre de la vacuna asignada
    def setNombreVacuna(self, nombreVacuna):
        self.__vacunaAsignada = nombreVacuna

    # Establece el enfermero que administra la vacuna
    def setEnfermeroVacuna(self, nombreEnfermero):
        self.__enfermeroVacuna = nombreEnfermero

    # Devuelve el enfermero que administra la vacuna
    def getEnfermeroVacuna(self):
        return self.__enfermeroVacuna

    # Introduce una dosis en la lista de vacunas del paciente
    def setVacuna(self, nombreVacuna):
        if nombreVacuna.lower() == "pfizer" or nombreVacuna.lower() == "moderna":
            for number in range(2):
                if self.__vacuna[number] == "":
                    self.__vacuna[number] = nombreVacuna.lower()
                    if self.__getDosisVacuna() == 2:
                        self.setFechaInmunidad()
                    break
        elif nombreVacuna.lower() == "johnson & johnson":
            self.__vacuna[0] = nombreVacuna.lower()
            self.setFechaInmunidad()

    # Devuelve las vacunas administradas al paciente
    def getVacunas(self):
        if self.__vacuna[0] != "" and self.__vacuna[1] == "":
            return self.__vacuna[0] + "."
        elif self.__vacuna[0] != "" and self.__vacuna[1] != "":
            return self.__vacuna[0] + ", " + self.__vacuna[1] + "."
        else:
            return ""

 # Métodos relacionados con la cita de la prueba solicitada

    # Devuelve el nombre de la prueba solicitada
    def getPruebaSolicitada(self):
        return self.__pruebaSolicitada

    # Elimina todos los datos relacionados con la cita de la prueba
    def deletePruebaSolicitada(self):
        self.__fechaCitaPrueba = ""
        self.__pruebaSolicitada = ""
        self.__enfermeroPrueba = ""
        self.__tecnicoAsignado = ""

    # Devuelve la fecha de la cita para la prueba
    def getFechaCitaPrueba(self):
        return self.__fechaCitaPrueba

    # Establece la fecha de la cita de la prueba
    def setFechaCitaPrueba(self, year, month, day):
        self.__fechaCitaPrueba = date(year, month, day)

    # Establece la fecha en la que se hizo el test serologico
    def setFechaTestSerologico(self, fecha):
        self.__fechaCitaPrueba = fecha

    # Establece el nombre de la prueba
    def setNombrePrueba(self, nombrePrueba):
        self.__pruebaSolicitada = nombrePrueba

    # Establece el tecnico que comprueba la prueba
    def setTecnicoSolicitado(self, nombreTecnico):
        self.__tecnicoAsignado = nombreTecnico

    # Establece el enfermero que realiza la prueba
    def setEnfermeroPrueba(self, nombreEnfermero):
        self.__enfermeroPrueba = nombreEnfermero

    # Devuelve el nombre del enfermero que realiza la prueba
    def getEnfermeroPrueba(self):
        return self.__enfermeroPrueba

    # Devuelve el nombre del tecnico que realiza la prueba
    def getTecnicoAsignado(self):
        return self.__tecnicoAsignado


# __Clase para instanciar enfermeros__
class Enfermero(Persona):
    def __init__(self, nombre, apellido1, apellido2):
        super().__init__(nombre, apellido1, apellido2)

    # Imprime una lista de las pruebas realizadas
    def printPruebasRealizadas(self, baseDatos, nombrePrueba):

        # Comprueba los datos introducidos
        if baseDatos.getPruebasRealizadas(nombrePrueba.lower()):
            for prueba in baseDatos.getPruebasRealizadas(nombrePrueba.lower()):
                key = int(prueba)
                # Imprime los datos de las pcr
                if nombrePrueba.lower() == "pcr":
                    if baseDatos.getPCR(key).getNombreEnfermero() == self.getNombre():
                        print(f"Nombre: {baseDatos.getPCR(key).getNombrePaciente()}. Fecha cita prueba: {baseDatos.getPCR(key).getFechaPrueba()}. Prueba solicitada: {baseDatos.getPCR(key).getNombrePrueba()}. Fecha final cuarentena: {baseDatos.buscarPaciente(baseDatos.getPCR(key).getNombrePaciente()).getFinCuarentena()}.")
                elif nombrePrueba.lower() == "antigenos":
                    if baseDatos.getAntigeno(key).getNombreEnfermero() == self.getNombre():
                        print(f"Nombre: {baseDatos.getAntigeno(key).getNombrePaciente()}. Fecha cita prueba: {baseDatos.getAntigeno(key).getFechaPrueba()}. Prueba solicitada: {baseDatos.getAntigeno(key).getNombrePrueba()}. Fecha final cuarentena: {baseDatos.buscarPaciente(baseDatos.getAntigeno(key).getNombrePaciente()).getFinCuarentena()}.")
                elif nombrePrueba.lower() == "serologico":
                    if baseDatos.getSerologico(key).getNombreEnfermero() == self.getNombre():
                        print(f"Nombre: {baseDatos.getSerologico(key).getNombrePaciente()}. Fecha cita prueba: {baseDatos.getSerologico(key).getFechaPrueba()}. Prueba solicitada: {baseDatos.getSerologico(key).getNombrePrueba()}. Fecha final cuarentena: {baseDatos.buscarPaciente(baseDatos.getSerologico(key).getNombrePaciente()).getFinCuarentena()}.")
        else:
            print("No hay pruebas almacenadas")

    # Imprime una lista de las vacunas realizadas
    def printVacunasRealizadas(self, baseDatos):
        if baseDatos.getVacunasAdministradas():
            for vacuna in baseDatos.getVacunasAdministradas():
                if vacuna.getNombreEnfermero() == self.getNombre():
                    print(
                        f"Nombre: {vacuna.getNombrePaciente()}. Fecha administracion: {vacuna.getFechaVacuna()}. Vacuna administrada: {vacuna.getNombreVacuna()}.")
        else:
            print("No hay vacunas almacenadas")

    # Crea una instancia de una prueba según el tipo de prueba introducido como parámentro y lo almacena en las listas correspondientes
    def realizarPruebas(self, baseDatos, nombrePrueba, nombrePaciente, nombreTecnico):
        if baseDatos.existePersona(nombrePaciente, baseDatos.getPacientes()) and baseDatos.existePersona(nombreTecnico, baseDatos.getTecnicos()):
            if nombrePrueba.lower() == "pcr":
                baseDatos.addPruebaPCR(prueba.PCR(
                    nombrePaciente, self.getNombre(), nombreTecnico))
            elif nombrePrueba.lower() == "antigenos":
                baseDatos.addPruebaAntigenos(prueba.Antigenos(
                    nombrePaciente, self.getNombre(), nombreTecnico))
            elif nombrePrueba.lower() == "serologico":
                baseDatos.addPruebaSerologica(prueba.Serologico(
                    nombrePaciente, self.getNombre(), nombreTecnico))
        else:
            print("Datos incorrectos")

    # Crea una instancia del tipo de vacuna añadida como parámetro y la añade a la lista correspondiente
    def administrarVacuna(self, baseDatos, nombreVacuna, nombrePaciente):
        if baseDatos.existePersona(nombrePaciente, baseDatos.getPacientes()):
            baseDatos.setVacuna(nombreVacuna, nombrePaciente, self.getNombre())
            baseDatos.buscarPaciente(nombrePaciente).setVacuna(nombreVacuna)
            baseDatos.buscarPaciente(nombrePaciente).deleteVacunaAsignada()
        else:
            print("Los datos introducidos no son correctos")

    # Imprime una lista de todos los pacientes asociados al enfermero
    def printListaPacientes(self, baseDatos):
        baseDatos.printListaXSanitario(self.getNombre(), "enfermero")


# __Clase para instanciar los técnicos de laboratorio__
class TecnicoDeLaboratorio(Persona):
    def __init__(self, nombre, apellido1, apellido2):
        super().__init__(nombre, apellido1, apellido2)

 # Métodos

    # Imprime una lista de las pruebas procesadas por el técnico
    def printPruebasProcesadas(self, baseDatos):
        # Imprime pruebas pcr
        if baseDatos.getPruebasRealizadas("pcr"):
            for pcr in baseDatos.getPruebasRealizadas("pcr"):
                key = int(pcr)
                if baseDatos.getPCR(key).getNombreTecnico() == self.getNombre():
                    print(f"Nombre: {baseDatos.getPCR(key).getNombrePaciente()}. Fecha cita prueba: {str(baseDatos.getPCR(key).getFechaPrueba())}. Prueba solicitada: {baseDatos.getPCR(key).getNombrePrueba()}. Codigo de la prueba: {key}. Procesada: {baseDatos.getPCR(key).getProcesada()}. Positivo: {baseDatos.getPCR(key).getPositivo()}.")

        # Imprime pruebas de antigenos
        if baseDatos.getPruebasRealizadas("antigenos"):
            for antigeno in baseDatos.getPruebasRealizadas("antigenos"):
                key = int(antigeno)
                if baseDatos.getAntigeno(key).getNombreTecnico() == self.getNombre():
                    print(f"Nombre: {baseDatos.getAntigeno(key).getNombrePaciente()}. Fecha cita prueba: {str(baseDatos.getAntigeno(key).getFechaPrueba())}. Prueba solicitada: {baseDatos.getAntigeno(key).getNombrePrueba()}. Codigo de la prueba: {key}. Procesada: {baseDatos.getAntigeno(key).getProcesada()}. Positivo: {baseDatos.getAntigeno(key).getPositivo()}.")

        # Imprime pruebas serologicas
        if baseDatos.getPruebasRealizadas("serologico"):
            for serologico in baseDatos.getPruebasRealizadas("serologico"):
                key = int(serologico)
                if baseDatos.getSerologico(key).getNombreTecnico() == self.getNombre():
                    print(f"Nombre: {baseDatos.getSerologico(key).getNombrePaciente()}. Fecha cita prueba: {str(baseDatos.getSerologico(key).getFechaPrueba())}. Prueba solicitada: {baseDatos.getSerologico(key).getNombrePrueba()}. Codigo de la prueba: {key}. Procesada: {baseDatos.getSerologico(key).getProcesada()}. Positivo: {baseDatos.getSerologico(key).getPositivo()}.")
        else:
            print("No hay pruebas almacenadas")

    # Establece el resultado de una prueba realizada (pcr o antigenos) y el estado del paciente
    def resultadoPrueba(self, baseDatos, nombrePaciente, nombrePrueba, key, positivo):

        # Se comprueba que los datos introducidos son correctos:
        if baseDatos.existePersona(nombrePaciente, baseDatos.getPacientes()) and nombrePrueba.lower() == "pcr" or nombrePrueba.lower() == "antigenos":

            # Se establece el resultado de la prueba
            if nombrePrueba.lower() == "pcr":
                baseDatos.getPCR(key).setPositivo(positivo)
                baseDatos.getPCR(key).setProcesada(True)

            elif nombrePrueba.lower() == "antigenos":
                baseDatos.getAntigeno(key).setPositivo(positivo)
                baseDatos.getAntigeno(key).setProcesada(True)

            # Si el paciente está contagiado se establece una cita automáticamente para realizar un test serológico
            if positivo:
                baseDatos.buscarPaciente(
                    nombrePaciente).setPacienteContagiado()
                baseDatos.buscarPaciente(nombrePaciente).setFechaTestSerologico(
                    baseDatos.buscarPaciente(nombrePaciente).getFinCuarentena())
                baseDatos.buscarPaciente(
                    nombrePaciente).setNombrePrueba("serologico")
                baseDatos.buscarPaciente(nombrePaciente).setEnfermeroPrueba(
                    baseDatos.buscarPaciente(nombrePaciente).getEnfermeroPrueba())
                baseDatos.buscarPaciente(nombrePaciente).setTecnicoSolicitado(
                    baseDatos.buscarPaciente(nombrePaciente).getTecnicoAsignado())
            else:
                baseDatos.buscarPaciente(
                    nombrePaciente).deletePruebaSolicitada()

        else:
            print("Nombre del paciente incorrecto")

    # Establece el resultado de una prueba serologica y la inmunidad del paciente
    def resultadoPruebaSerologica(self, baseDatos, nombrePaciente, key, anticuerpos):

        if baseDatos.existePersona(nombrePaciente, baseDatos.getPacientes()):

            # Registra el número de anticuerpos obtenidos en la prueba
            baseDatos.getSerologico(key).setAnticuerpos(anticuerpos)
            baseDatos.getSerologico(key).setProcesada(True)

            # Establece hasta cuándo el paciente tendrá inmunidad en el caso de tenerla
            if anticuerpos > 2:
                baseDatos.getSerologico(key).setPositivo(True)
                baseDatos.buscarPaciente(nombrePaciente).setFechaInmunidad()
            else:
                baseDatos.getSerologico(key).setPositivo(False)
                baseDatos.buscarPaciente(nombrePaciente).setFechaInmunidad()

            baseDatos.buscarPaciente(nombrePaciente).deletePruebaSolicitada()

        else:
            print("Los datos del paciente introducidos no son correctos")


# __Clase para instanciar al administrador__
class Administrador(Persona):
    def __init__(self, nombre, apellido1, apellido2):
        super().__init__(nombre, apellido1, apellido2)

 # Métodos

    def altaPersona(self, baseDatos, clasePersona, nombre, apellido1, apellido2):
        if clasePersona.lower() == "paciente":
            paciente = Paciente(nombre, apellido1, apellido2)
            baseDatos.addPersona(paciente, baseDatos.getPacientes())
        elif clasePersona.lower() == "enfermero" or clasePersona.lower() == "enfermera":
            enfermero = Enfermero(nombre, apellido1, apellido2)
            baseDatos.addPersona(enfermero, baseDatos.getEnfermeros())
        elif clasePersona.lower() == "tecnico":
            tecnico = TecnicoDeLaboratorio(nombre, apellido1, apellido2)
            baseDatos.addPersona(tecnico, baseDatos.getTecnicos())
        else:
            print("La clase de persona introducida no es correcta")

    # Corrige el nombre de una persona
    def corregirNombrePersona(self, baseDatos, clasePersona, nombrePersona, nombre, apellido1, apellido2):
        if clasePersona.lower() == "paciente":
            baseDatos.buscarPaciente(nombrePersona).setNombre(
                nombre, apellido1, apellido2)
        elif clasePersona.lower() == "enfermero" or clasePersona.lower() == "enfermera":
            baseDatos.buscarEnfermero(nombrePersona).setNombre(
                nombre, apellido1, apellido2)
        elif clasePersona.lower() == "tecnico":
            baseDatos.buscarTecnico(nombrePersona).setNombre(
                nombre, apellido1, apellido2)
        else:
            print("La clase de persona introducida no es correcta")

    # Borra la persona introducida como parámetro
    def borrarPersona(self, baseDatos, clasePersona, nombre):
        if clasePersona.lower() == "paciente":
            baseDatos.deletePersona(nombre, baseDatos.getPacientes())
        elif clasePersona.lower() == "enfermero" or clasePersona.lower() == "enfermera":
            baseDatos.deletePersona(nombre, baseDatos.getEnfermeros())
        elif clasePersona.lower() == "tecnico":
            baseDatos.deletePersona(nombre, baseDatos.getTecnicos())
        else:
            print("La clase de persona introducida no es correcta")

    # Asigna una cita para una prueba a un paciente
    def setCitaPrueba(self, baseDatos, nombrePaciente, nombrePrueba, year, month, day, nombreEnfermero, nombreTecnico):
        if baseDatos.existePersona(nombrePaciente, baseDatos.getPacientes()) and baseDatos.existePersona(nombreEnfermero, baseDatos.getEnfermeros()) and baseDatos.existePersona(nombreTecnico, baseDatos.getTecnicos()):
            baseDatos.buscarPaciente(
                nombrePaciente).setFechaCitaPrueba(year, month, day)
            baseDatos.buscarPaciente(
                nombrePaciente).setEnfermeroPrueba(nombreEnfermero)
            baseDatos.buscarPaciente(
                nombrePaciente).setTecnicoSolicitado(nombreTecnico)
            baseDatos.buscarPaciente(
                nombrePaciente).setNombrePrueba(nombrePrueba)
        else:
            print("Los datos introducidos no son correctos")

    # Asigna una cita para administrar una vacuna al paciente
    def setCitaVacuna(self, baseDatos, nombrePaciente, nombreVacuna, year, month, day, nombreEnfermero):
        if baseDatos.existePersona(nombrePaciente, baseDatos.getPacientes()) and baseDatos.existePersona(nombreEnfermero, baseDatos.getEnfermeros()):
            baseDatos.buscarPaciente(
                nombrePaciente).setFechaCitaVacuna(year, month, day)
            baseDatos.buscarPaciente(
                nombrePaciente).setEnfermeroVacuna(nombreEnfermero)
            baseDatos.buscarPaciente(
                nombrePaciente).setNombreVacuna(nombreVacuna)
        else:
            print("Los datos introducidos no son correctos")

    # Imprime todos los pacientes asignados a un enfermero
    def printPacientesEnfermeros(self, baseDatos, nombreSanitario):
        tipoSanitario = "enfermero"
        baseDatos.printListaXSanitario(nombreSanitario, tipoSanitario)

    # Imprime todos los pacientes asignados a un tecnico
    def printPacientesTecnico(self, baseDatos, nombreSanitario):
        tipoSanitario = "tecnico"
        baseDatos.printListaXSanitario(nombreSanitario, tipoSanitario)

    # Imprime una lista de los pacientes confinados
    def printPacientesConfinados(self, baseDatos):
        for paciente in baseDatos.getPacientes():
            if paciente.getPacienteContagiado():
                print(
                    f"Nombre: {paciente.getNombre()}. Fecha final cuarentena: {paciente.getFechaFinCuarentena()}.")
