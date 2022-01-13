import base_datos
import persona


# __Clase que sirve para instanciar un objeto que almacene todos los comandos de la interfaz
class Comandos:
    def __init__(self):
        self.__comandosGeneral = ["quit", "abrir sesion", "help"]
        self.__comandosAdministrador = ["add paciente", "add tecnico", "add enfermero", "corregir paciente", "corregir enfermero", "corregir tecnico", "cita prueba", "cita vacuna",
                                        "pacientes enfermero", "pacientes tecnico", "pacientes confinados", "logout", "help", "borrar paciente", "borrar enfermero", "borrar tecnico"]
        self.__comandosEnfermero = ["lista pcr", "lista antigenos", "lista serologicas", "lista vacunas", "lista pacientes",
                                    "realizar pcr", "realizar antigenos", "realizar serologica", "administrar pfizer", "administrar moderna", "administrar johnson", "logout", "help"]
        self.__comandosTecnico = ["lista pruebas", "resultado pcr",
                                  "resultado antigenos", "resultado serologico", "logout", "help"]

 # Métodos

    # Analiza si es comando general
    def esComandoGeneral(self, string):
        esComando = False

        for comando in self.__comandosGeneral:
            if comando == string:
                esComando = True

        return esComando

    # Analiza si el comando introducido pertenece al administrador
    def esComandoAdministrador(self, string):
        esComando = False

        for comando in self.__comandosAdministrador:
            if comando == string:
                esComando = True

        return esComando

    # Analiza si el comando introducido pertenece al enfermero
    def esComandoEnfermero(self, string):
        esComando = False

        for comando in self.__comandosEnfermero:
            if comando == string:
                esComando = True

        return esComando

    # Analiza si el comando introducido pertenece al tecnico
    def esComandoTecnico(self, string):
        esComando = False

        for comando in self.__comandosTecnico:
            if comando == string:
                esComando = True

        return esComando

    # Imprime todos los comandos generales
    def mostrarComandosGenerales(self):
        print(', '.join(map(str, self.__comandosGeneral)))

    # Imprime todos los comandos pertenecientes al administrador
    def mostrarComandosAministrador(self):
        print(', '.join(map(str, self.__comandosAdministrador)))

    # Imprime los comandos pertenecientes al enfermero
    def mostrarComandosEnfermero(self):
        print(', '.join(map(str, self.__comandosEnfermero)))

    # Imprime los comandos pertenecientes al tecnico
    def mostrarComandosTecnico(self):
        print(', '.join(map(str, self.__comandosTecnico)))


# __Clase para instanciar objetos que comprueben si los comandos introducidos en la interfaz son válidos o no
class Analizador:
    def __init__(self):
        self.__comandos = Comandos()

 # Metodos

    # Devuelve el comando introducido por el usuario
    def getComando(self):
        comando = input("> ")
        return comando

    # Analiza si el comando pertenece a los comandos generales
    def getComandoGeneral(self):
        comando = self.getComando()

        if self.__comandos.esComandoGeneral(comando):
            return comando

    # Analiza si el comando pertenece a los comandos del administrador
    def getComandoAdministrador(self):
        comando = self.getComando()

        if self.__comandos.esComandoAdministrador(comando):
            return comando

    # Analiza si el comando pertenece a los comandos del enfermero
    def getComandoEnfermero(self):
        comando = self.getComando()

        if self.__comandos.esComandoEnfermero(comando):
            return comando

    # Analiza si el comando pertenece a los comandos del tecnico
    def getComandoTecnico(self):
        comando = self.getComando()

        if self.__comandos.esComandoTecnico(comando):
            return comando

    # Imprime los comandos validos para la pantalla general
    def mostrarComandosGenerales(self):
        self.__comandos.mostrarComandosGenerales()

    # Imprime los comandos validos para el perfil del administrador
    def mostrarComandosAdministrador(self):
        self.__comandos.mostrarComandosAministrador()

    # Imprime los comandos validos para el perfil de enfermero
    def mostrarComandosEnfermero(self):
        self.__comandos.mostrarComandosEnfermero()

    # Imprime los comandos validos para el perfil de tecnico
    def mostrarComandosTecnico(self):
        self.__comandos.mostrarComandosTecnico()


# __Clase para instanciar un objeto que represente a la interfaz de usuario
class Interfaz:
    def __init__(self):
        self.__analizador = Analizador()
        self.__baseDatos = base_datos.BaseDatos()
        self.__administrador: persona.Administrador
        self.__tecnico: persona.TecnicoDeLaboratorio
        self.__enfermero: persona.Enfermero
        self.__acabar = False

 # Métodos

  # Funciones para introducir nombres y apellidos

    def __introducirNombre(self):
        print("Nombre:")
        nombrePersona = input("> ")

        if nombrePersona == "":
            raise ValueError("El nombre no puede estar vacio")

        return nombrePersona

    def __introducirApellido1(self):
        print("Primer apellido:")
        apellido1 = input("> ")

        if apellido1 == "":
            raise ValueError("El primer apellido no puede estar vacio")

        return apellido1

    def __introducirApellido2(self):
        print("Segundo apellido:")
        apellido2 = input("> ")

        if apellido2 == "":
            raise ValueError("El segundo apellido no puede estar vacio")

        return apellido2

  # Funcion para cerrar el programa
    def __quit(self):
        print("")
        return True

  # Métodos del administrador

    # Ejecuta la interfaz del administrador
    def __interfazAdministrador(self):
        print("Ha iniciado sesion como administrador")

        acabar = False

        while not acabar:
            comando = self.__analizador.getComandoAdministrador()

            if comando:
                acabar = self.__procesarComandoAdministrador(comando)
            else:
                print("Comando desconocido")

        print("Sesion cerrada")

    # Procesa los comandos introducidos como administrador
    def __procesarComandoAdministrador(self, comando):

        salir = False

        if comando.lower() == "help":
            self.__printHelpAdminsitrador()
        elif comando.lower() == "logout":
            salir = self.__quit()
        elif comando.lower() == "add paciente":
            self.__addPaciente()
        elif comando.lower() == "add enfermero":
            self.__addEnfermero()
        elif comando.lower() == "add tecnico":
            self.__addTecnico()
        elif comando.lower() == "borrar paciente":
            self.__borrarPaciente()
        elif comando.lower() == "borrar enfermero":
            self.__borrarEnfermero()
        elif comando.lower() == "borrar tecnico":
            self.__borrarTecnico()
        elif comando.lower() == "corregir paciente":
            self.__corregirPaciente()
        elif comando.lower() == "corregir enfermero":
            self.__corregirEnfermero()
        elif comando.lower() == "corregir tecnico":
            self.__corregirTecnico()
        elif comando.lower() == "cita prueba":
            self.__citaPrueba()
        elif comando.lower() == "cita vacuna":
            self.__citaVacuna()
        elif comando.lower() == "pacientes enfermero":
            self.__pacientesEnfermero()
        elif comando.lower() == "pacientes tecnico":
            self.__pacientesTecnico()
        elif comando.lower() == "pacientes confinados":
            self.__pacientesConfinados()

        return salir

    def __printHelpAdminsitrador(self):
        self.__analizador.mostrarComandosAdministrador()

    def __addPaciente(self):
        try:
            self.__administrador.altaPersona(
                self.__baseDatos, "paciente", self.__introducirNombre(), self.__introducirApellido1(), self.__introducirApellido2())
            print("Paciente creado")
        except ValueError as e:
            print(e)

    def __addEnfermero(self):
        try:
            self.__administrador.altaPersona(self.__baseDatos, "enfermero", self.__introducirNombre(
            ), self.__introducirApellido1(), self.__introducirApellido2())
            print("Enfermero creado")
        except ValueError as e:
            print(e)

    def __addTecnico(self):
        try:
            self.__administrador.altaPersona(self.__baseDatos, "tecnico", self.__introducirNombre(
            ), self.__introducirApellido1(), self.__introducirApellido2())
            print("Tecnico creado")
        except ValueError as e:
            print(e)

    def __borrarPaciente(self):
        try:
            print("Nombre del paciente:")
            self.__administrador.borrarPersona(
                self.__baseDatos, "paciente", input("> ").lower())
            print("Paciente borrado")
            print("")
        except ValueError as e:
            print(e)

    def __borrarEnfermero(self):
        try:
            print("Nombre del enfermero/a:")
            self.__administrador.borrarPersona(
                self.__baseDatos, "enfermero", input("> ").lower())
            print("Enfermero/a borrado/a")
            print("")
        except ValueError as e:
            print(e)

    def __borrarTecnico(self):
        try:
            print("Nombre del tecnico:")
            self.__administrador.borrarPersona(
                self.__baseDatos, "tecnico", input("> ").lower())
            print("Tecnico borrado")
            print("")
        except ValueError as e:
            print(e)

    def __corregirPaciente(self):
        nombreActual = ""
        print("Nombre actual:")

        try:
            nombreActual = input("> ")
            # Corregir datos
            self.__administrador(self.__baseDatos, "paciente", nombreActual, self.__introducirNombre(
            ), self.__introducirApellido1(), self.__introducirApellido2())
            print("Paciente corregido")
        except ValueError as e:
            print(e)

    def __corregirEnfermero(self):
        nombreActual = ""
        print("Nombre actual:")

        try:
            nombreActual = input("> ")
            # Corregir datos
            self.__administrador(self.__baseDatos, "enfermero", nombreActual, self.__introducirNombre(
            ), self.__introducirApellido1(), self.__introducirApellido2())
            print("Enfermero corregido")
        except ValueError as e:
            print(e)

    def __corregirTecnico(self):
        nombreActual = ""
        print("Nombre actual:")

        try:
            nombreActual = input("> ")
            # Corregir datos
            self.__administrador(self.__baseDatos, "tecnico", nombreActual, self.__introducirNombre(
            ), self.__introducirApellido1(), self.__introducirApellido2())
            print("Tecnico corregido")
        except ValueError as e:
            print(e)

    def __citaPrueba(self):
        nombrePaciente: str
        prueba: str
        dia: int
        mes: int
        anno: int
        nombreEnfermero: str
        nombreTecnico: str

        try:
            print("Nombre del paciente:")
            nombrePaciente = input("> ")

            print("Nombre de la prueba:")
            prueba = input("> ")

            print("Dia:")
            dia = int(input("> "))

            print("Mes:")
            mes = int(input("> "))

            print("Anno:")
            anno = int(input("> "))

            print("Nombre del enfermero:")
            nombreEnfermero = input("> ")

            print("Nombre del tecnico")
            nombreTecnico = input("> ")

            # Introduce todos los datos recogidos como parametros en el metodo del administrado
            self.__administrador.setCitaPrueba(self.__baseDatos, nombrePaciente.lower(
            ), prueba.lower(), anno, mes, dia, nombreEnfermero.lower(), nombreTecnico.lower())
            print("Cita para prueba creada")

        except ValueError as e:
            print(e)

        print("")

    def __citaVacuna(self):
        nombrePaciente: str
        vacuna: str
        dia: int
        mes: int
        anno: int
        nombreEnfermero: str

        try:
            print("Nombre del paciente:")
            nombrePaciente = input("> ")

            print("Nombre de la vacuna:")
            vacuna = input("> ")

            print("Dia:")
            dia = int(input("> "))

            print("Mes:")
            mes = int(input("> "))

            print("Anno:")
            anno = int(input("> "))

            print("Nombre del enfermero:")
            nombreEnfermero = input("> ")

            # Introduce todos los datos recogidos como parametros en el metodo del administrado
            self.__administrador.setCitaVacuna(self.__baseDatos, nombrePaciente.lower(
            ), vacuna.lower(), anno, mes, dia, nombreEnfermero.lower())
            print("Cita para vacuna creada")

        except ValueError as e:
            print(e)

        print("")

    def __pacientesEnfermero(self):
        try:
            print("Nombre del enfermero:")
            self.__administrador.printPacientesEnfermeros(
                self.__baseDatos, input("> ").lower())
            print("")
        except ValueError as e:
            print(e)

    def __pacientesTecnico(self):
        try:
            print("Nombre del tecnico:")
            self.__administrador.printPacientesTecnico(
                self.__baseDatos, input("> ").lower())
            print("")
        except ValueError as e:
            print(e)

    def __pacientesConfinados(self):
        self.__administrador.printPacientesConfinados(self.__baseDatos)
        print("")

  # Métodos del enfermero

    def __interfazEnfermero(self):
        print("Ha iniciado sesion como enfermero")

        acabar = False

        while not acabar:
            comando = self.__analizador.getComandoEnfermero()

            if comando:
                acabar = self.__procesarComandoEnfermero(comando)
            else:
                print("Comando desconocido")

        print("Sesion cerrada")

    def __procesarComandoEnfermero(self, comando):
        salir = False

        if comando == "help":
            self.__printHelpEnfermero()

        elif comando == "logout":
            salir = self.__quit()
            self.__enfermero: persona.Enfermero

        elif comando == "lista pcr":
            self.__printPCR()

        elif comando == "lista antigenos":
            self.__printAntigenos()

        elif comando == "lista serologicas":
            self.__printSerologicos()

        elif comando == "lista vacunas":
            self.__printVacunas()

        elif comando == "lista pacientes":
            self.__pacientes()

        elif comando == "realizar pcr":
            self.__realizarPCR()

        elif comando == "realizar antigenos":
            self.__realizarAntigenos()

        elif comando == "realizar serologica":
            self.__realizarSerologica()

        elif comando == "administrar pfizer":
            self.__administrarPfizer()

        elif comando == "administrar moderna":
            self.__administrarModerna()

        elif comando == "administrar johnson":
            self.__administrarJohnson()

        return salir

    def __printHelpEnfermero(self):
        self.__analizador.mostrarComandosEnfermero()
        print("")

    def __printPCR(self):
        self.__enfermero.printPruebasRealizadas(self.__baseDatos, "pcr")
        print("")

    def __printAntigenos(self):
        self.__enfermero.printPruebasRealizadas(self.__baseDatos, "antigenos")
        print("")

    def __printSerologicos(self):
        self.__enfermero.printPruebasRealizadas(self.__baseDatos, "serologico")
        print("")

    def __printVacunas(self):
        self.__enfermero.printVacunasRealizadas(self.__baseDatos)
        print("")

    def __pacientes(self):
        self.__enfermero.printListaPacientes(self.__baseDatos)
        print("")

    def __realizarPCR(self):
        try:
            print("Paciente:")
            paciente = input("> ")
            print("Tecnico:")
            tecnico = input("> ")

            self.__enfermero.realizarPruebas(
                self.__baseDatos, "pcr", paciente, tecnico)
        except ValueError as e:
            print(e)

        print("")

    def __realizarAntigenos(self):
        try:
            print("Paciente:")
            paciente = input("> ")
            print("Tecnico:")
            tecnico = input("> ")

            self.__enfermero.realizarPruebas(
                self.__baseDatos, "antigenos", paciente, tecnico)
        except ValueError as e:
            print(e)

        print("")

    def __realizarSerologica(self):
        try:
            print("Paciente:")
            paciente = input("> ")
            print("Tecnico:")
            tecnico = input("> ")

            self.__enfermero.realizarPruebas(
                self.__baseDatos, "serologico", paciente, tecnico)
        except ValueError as e:
            print(e)

        print("")

    def __administrarPfizer(self):
        try:
            print("Paciente:")
            paciente = input("> ")

            self.__enfermero.administrarVacuna(
                self.__baseDatos, "pfizer", paciente)

        except ValueError as e:
            print(e)

        print("")

    def __administrarModerna(self):
        try:
            print("Paciente:")
            paciente = input("> ")

            self.__enfermero.administrarVacuna(
                self.__baseDatos, "moderna", paciente)

        except ValueError as e:
            print(e)

        print("")

    def __administrarJohnson(self):
        try:
            print("Paciente:")
            paciente = input("> ")

            self.__enfermero.administrarVacuna(
                self.__baseDatos, "johnson & johnson", paciente)

        except ValueError as e:
            print(e)

        print("")

  # Métodos del técnico

    def __interfazTecnico(self):
        print("Ha iniciado sesion como tecnico")

        acabar = False

        while not acabar:
            comando = self.__analizador.getComandoTecnico()

            if comando:
                acabar = self.__procesarComandoTecnico()
            else:
                print("Comando desconocido")

        print("Sesion cerrada")

    def __procesarComandoTecnico(self, comando):

        salir = False

        if comando == "help":
            self.__printHelpTecnico()
            print("")

        elif comando == "logout":
            salir = self.__quit()
            self.__tecnico: persona.TecnicoDeLaboratorio()

        elif comando == "resultado pcr":
            self.__resultadoPCR()

        elif comando == "resultado antigenos":
            self.__resultadoAntigenos()

        elif comando == "resultado serologico":
            self.__resultadoSerologico()

        elif comando == "lista pruebas":
            self.__listaPruebas()

        return salir

    def __listaPruebas(self):
        self.__tecnico.printPruebasProcesadas(self.__baseDatos)
        print("")

    def __resultadoPCR(self):

        positivoBooleano = False
        nombre: str
        codigo: str
        positivo: str

        try:
            print("Paciente:")
            nombre = input("> ")
            print("Codigo de la prueba")
            codigo = input("> ")
            print("Positivo (true/false):")
            positivo = input("> ")

            if positivo.lower() == "true" or positivo.lower() == "false":
                if positivo.lower() == "true":
                    positivoBooleano = True
                self.__tecnico.resultadoPrueba(
                    self.__baseDatos, nombre, "pcr", codigo, positivoBooleano)
            else:
                print("Datos incorrectos")

        except ValueError as e:
            print(e)

    def __resultadoAntigenos(self):

        positivoBooleano = False
        nombre: str
        codigo: str
        positivo: str

        try:
            print("Paciente:")
            nombre = input("> ")
            print("Codigo de la prueba")
            codigo = input("> ")
            print("Positivo (true/false):")
            positivo = input("> ")

            if positivo.lower() == "true" or positivo.lower() == "false":
                if positivo.lower() == "true":
                    positivoBooleano = True
                self.__tecnico.resultadoPrueba(
                    self.__baseDatos, nombre, "antigenos", codigo, positivoBooleano)
            else:
                print("Datos incorrectos")

        except ValueError as e:
            print(e)

    def __resultadoSerologico(self):

        positivoBooleano = False
        nombre: str
        codigo: str
        anticuerpos: int

        try:
            print("Paciente:")
            nombre = input("> ")
            print("Codigo de la prueba")
            codigo = input("> ")
            print("Anticuerpos /de 0 a 10):")
            anticuerpos = int(input("> "))

            self.__tecnico.resultadoPruebaSerologica(
                self.__baseDatos, nombre, codigo, anticuerpos)

        except ValueError as e:
            print(e)

        print("")

    def __printHelpTecnico(self):
        self.__analizador.mostrarComandosTecnico()
        print("")

  # Ejecución del programa

    # Permite registrar un administrador cuando el programa se ejecuta por primera vez

    def inicioAdministrador(self):
        acabar = False

        try:
            print("Iniciado el registro del administrador")
            self.__administrador = persona.Administrador(self.__introducirNombre(
            ), self.__introducirApellido1(), self.__introducirApellido2())
            print("Administrador creado")

        except ValueError as e:
            print(e)

        print("")

    # Crea la primera pantalla de la interfaz en la que se pide el tipo de empleado y el nombre. Funciona en forma de bucle hasta que se introduce el comando quit
    def inicio(self):

        while(not self.__acabar):
            print("¿Que desea hacer?")
            comando = self.__analizador.getComandoGeneral()

            if comando:
                if comando == "help":
                    self.__analizador.mostrarComandosGenerales()

                elif comando == "abrir sesion":
                    print("Tipo de empleado")
                    tipoEmpleado = input("> ")

                    if not tipoEmpleado:
                        raise ValueError("No se puede dejar el campo vacio")
                    else:

                        print("Nombre:")
                        nombreEmpleado = input("> ")

                        if tipoEmpleado.lower() == "administrador":
                            if self.__administrador.getNombre().lower() == nombreEmpleado.lower():
                                self.__interfazAdministrador()
                            else:
                                print("Nombre incorrecto")

                        elif tipoEmpleado.lower() == "enfermero":
                            if self.__baseDatos.existePersona(nombreEmpleado, self.__baseDatos.getEnfermeros()):
                                self.__enfermero = self.__baseDatos.buscarEnfermero(
                                    nombreEmpleado)
                                self.__interfazEnfermero()
                            else:
                                print("El enfermero descrito no existe")

                        elif tipoEmpleado.lower() == "tecnico":
                            if self.__baseDatos.existePersona(nombreEmpleado, self.__baseDatos.getTecnicos()):
                                self.__tecnico = self.__baseDatos.buscarTecnico(
                                    nombreEmpleado)
                                self.__interfazTecnico()
                            else:
                                print("El tecnico descrito no existe")

                        else:
                            print("Empleado introducido incorrecto")

                        tipoEmpleado = None

                elif comando == "quit":
                    self.__acabar = True

                print("")

        print("Hasta pronto")
