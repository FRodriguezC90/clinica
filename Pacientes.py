from Personas import Personas

class Pacientes(Personas):
    def __init__(self,id, nombrecompleto, rut):
        super().__init__(id,nombrecompleto, rut)


    def __init__(self, id, usuario, clave):
        self.id = id
        self.usuario = usuario
        self.clave = clave
        


  