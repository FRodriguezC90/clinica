from mysql.connector import Connect,Error
from getpass import getpass
from conector import DataBase
from Personas import Personas
from Pacientes import Pacientes
from Profesionales import Profesional

#5 Cuentas de perfil paciente
pc1=Pacientes('2mastias','mastias123', 1,'Matias Gonzalez Perez', 18778932-6)
pc2=Pacientes('2carlos','carlos123', 2,'Carlos Jarpa Lopez', 15774232-1)
pc3=Pacientes('2fernando','fernando123', 3,'Fernando Marquez Letelier', 14776972-7)
pc4=Pacientes('2nicolas','nicolas123', 4,'Nicolas Ferrada Zabaleta', 16443567-8)
pc5=Pacientes('2tomas','tomas123', 5,'Tomas Ovalle Elgueta', 14112345-8)

print(pc1)

#5 Cuentas de perfil Profesional
pr1=Profesional('1andrea','andrea123', 6,'Andrea Pizarro Galvez', 19887654-6)
pr2=Profesional('2carla','carla123', 7,'Carla Aedo Vielma', 15332882-5)
pr3=Profesional('3mateo','mateo123', 8,'Mateo Lara Villa', 16112325-5)
pr4=Profesional('4camilo','camilo123', 9,'Camilo Zambrano Lara', 18332946-2)
pr5=Profesional('5patricio','patricio123', 10,'Patricio Galaz Andrade', 18332946-3)

Inicio=getpass("Bienvenido a Clinica Inacap... Presiona una tecla para continuar")
log = input("Ingrese usuario: ")
pwd = getpass("Ingrese su contraseña: ")


#db = DataBase(input("Ingrese nombre "),getpass("Ingrese Password "))
#db.conectar()