class Asignatura:
    def __init__(self, codigo, nombre, nota) -> None:
        self.__codigo = codigo
        self.__nombre = nombre
        self.__nota = nota

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        self.__nota = nota