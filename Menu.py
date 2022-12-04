from mysql.connector import connect,Error
from getpass import getpass
from conector import DataBase
from Pacientes import Pacientes
from Profesionales import Profesional

#5 Cuentas de perfil paciente
pc1=Pacientes('2paciente1','1paciente123', 1,'Matias Gonzalez Perez', 18778932-6)
pc2=Pacientes('2paciente2','2paciente123', 2,'Carlos Jarpa Lopez', 15774232-1)
pc3=Pacientes('2paciente3','3paciente123', 3,'Fernando Marquez Letelier', 14776972-7)
pc4=Pacientes('2paciente4','4paciente123', 4,'Nicolas Ferrada Zabaleta', 16443567-8)
pc5=Pacientes('2paciente5','5paciente123', 5,'Tomas Ovalle Elgueta', 14112345-8)

#5 Cuentas de perfil Profesional
pr1=Profesional('1doctor1','1doctor123', 6,'Andrea Pizarro Galvez', 19887654-6)
pr2=Profesional('1doctor2','2doctor123', 7,'Carla Aedo Vielma', 15332882-5)
pr3=Profesional('1doctor3','3doctor123', 8,'Mateo Lara Villa', 16112325-5)
pr4=Profesional('1doctor4','4doctor123', 9,'Camilo Zambrano Lara', 18332946-2)
pr5=Profesional('1doctor5','5doctor123', 10,'Patricio Galaz Andrade', 18332946-3)

Inicio=getpass("Bienvenido a Clinica Inacap... Presiona una tecla para continuar")
log = input("Ingrese usuario: ")
pwd = getpass("Ingrese su contraseña: ")

if log.startswith("1"):

        while True:
            print('''
            ===== Menu de opciones (Medico)=====
            1. Listar Pacientes
            2. Listar Agendas
            3. Añadir Paciente
            4. Modificar Agenda
            0. Salir    
                ''')
            op = input('Ingrese seleccion:\n')

            if op == '1':
                print("========Listar Pacientes========")
                input('Presione enter para continuar...')
                try:
                    with connect(
                        host="localhost",
                        user="root",
                        password="asdf",
                        database="mydb"
                    ) as connection:
                        print(connection)
                        select = ('SELECT a.Per_id, a.Per_nombrecompleto, a.Per_rut, p.Pac_usuario, p.Pac_clave FROM personas a JOIN pacientes p ON (a.Per_id = p.Pac_id)')
                        with connection.cursor() as cursor:
                            cursor.execute(select)
                            for row in cursor.fetchall():
                                print("ID - Nombres - RUT - Usuario - Clave")
                                print(row)
                except Error as e:
                                print(e)
                                break       
            elif op == '2':
                print("========Listar Agendas========")
                input('Presione enter para continuar...')
                try:
                    with connect(
                        host="localhost",
                        user="root",
                        password="asdf",
                        database="mydb"
                    ) as connection:
                        print(connection)
                        select = ('SELECT a.Agend_id, m.Medicos_usuario, a.Agend_paciente, a.Agend_fecha, a.Agend_hora FROM agendas a NATURAL JOIN medicos m')
                        with connection.cursor() as cursor:
                            cursor.execute(select)
                            for row in cursor.fetchall():
                                print("ID - Nombres - RUT - Usuario - Clave")
                                print(row)
                except Error as e:
                                print(e)
                                break 
            elif op == '3':
                print("========Añadir Pacientes========")
                input('Presione enter para continuar...')
                newname=input("ingrese Nombre Completo de Paciente")
                id=11
                rut=int(input("Ingrese Rut"))
                user=input("Ingrese nuevo usuario")
                psw=input("Ingrese nueva contraseña")
                try:
                    with connect(
                        host="localhost",
                        user="root",
                        password="asdf",
                        database="mydb"
                    ) as connection:
                        print(connection)
                        select = (f'INSERT into pacientes (Pac_id, Pac_usuario, Pac_clave) VALUES ({id}, {user}, {psw})')
                        with connection.cursor() as cursor:
                            cursor.execute(select)
                            for row in cursor.fetchall():
                                print("Ingreso de paciente correcto")
                                print(row)
                except Error as e:
                                print(e)
                                break 
            elif op == '4':
                print("=======Modificar Agendas========")
                input('Presione enter para continuar...')
            elif op == '0':
                print("========Listar Pacientes========")
                input('Presione enter para continuar...')
            
else:
        while True:
            print('''
            ===== Menu de opciones (Pacientes)=====
            1. Listar Pacientes
            2. Listar Agendas
            3. Añadir Paciente
            4. Modificar Agenda
            0. Salir    
                ''')
            op = input('Ingrese seleccion:\n')

            if op == '1':
                input('Presione enter para continuar...')
        
#db = DataBase(input("Ingrese nombre "),getpass("Ingrese Password "))
#db.conectar()