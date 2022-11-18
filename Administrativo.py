from Personas import Personas

class Funcionarios(Personas):
    def __init__(self, nombreCompleto, rut) -> None:
        super().__init__(nombreCompleto, rut)

    def __init__(self, usuario, clave):
        self.usuario = usuario
        self.clave = clave
        
