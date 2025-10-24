from DAO import DAO
from Empleado import Empleado
from Departamento import Departamento

dao = DAO()

def registrar_empleado():
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    fecha_inicio = input("Fecha de inicio (AAAA-MM-DD): ")
    salario = float(input("Salario: "))
    id_depto = int(input("ID Departamento: "))
    e = Empleado(None, nombre, direccion, telefono, email, fecha_inicio, salario, id_depto)
    dao.insertar_empleado(e)
    print("Empleado registrado.")

def mostrar_empleados():
    empleados = dao.obtener_empleados()
    for e in empleados:
        print(e)

def registrar_departamento():
    nombre = input("Nombre del departamento: ")
    gerente = input("Gerente: ")
    d = Departamento(None, nombre, gerente)
    dao.insertar_departamento(d)
    print("Departamento registrado.")

def mostrar_departamentos():
    departamentos = dao.obtener_departamentos()
    for d in departamentos:
        print(d)

def menu():
    while True:
        print("\n---- Menú Principal ----")
        print("1. Registrar Empleado")
        print("2. Mostrar Empleados")
        print("3. Registrar Departamento")
        print("4. Mostrar Departamentos")
        print("5. Salir")
        op = input("Opción: ")
        if op == "1":
            registrar_empleado()
        elif op == "2":
            mostrar_empleados()
        elif op == "3":
            registrar_departamento()
        elif op == "4":
            mostrar_departamentos()
        elif op == "5":
            break
        else:
            print("Opción inválida")

menu()
