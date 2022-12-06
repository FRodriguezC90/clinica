from Personas import *

class Profesional(Personas):
    def __init__(self, usuario, clave, id, nombrecompleto, rut):
        super().__init__(id,nombrecompleto, rut)
        self.usuario = usuario
        self.clave = clave


daniel = Profesional('1daniel','123fre',12,'Daniel Jofre','1800594-2')
print(daniel.nombrecompleto)