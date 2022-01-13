from interfaz import Interfaz


class Programa:
    def __init__(self):
        self.__interfaz = Interfaz()

    # Ejecuta el programa
    def main(self):

        self.__interfaz.inicioAdministrador()
        self.__interfaz.inicio()


programa = Programa()
programa.main()
