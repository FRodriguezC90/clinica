from Personas import *

class Pacientes(Personas):
    def __init__(self, usuario, clave, id, nombrecompleto, rut):
        super().__init__(id,nombrecompleto, rut)
        self.usuario = usuario
        self.clave = clave
    
    def descripciontotal(self):
        print("Usuario: ", self.usuario, "Clave: ", self.clave, "ID: ", self.id, "Nombre: ", self.nombrecompleto, "RUT: ", self.rut)


pc5=Pacientes('2tomas','tomas123', 5,'Tomas Ovalle Elgueta', 14112345-8)

print(pc5.descripciontotal)