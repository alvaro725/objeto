import re
from DAO import DAO
from Usuario import Usuario
from Empleado import Empleado
from Departamento import Departamento
from Proyecto import Proyecto
from decimal import Decimal
from datetime import datetime

dao = DAO()

# ===================================================
# LOGIN + REGISTRO
# ===================================================
def registrar_usuario():
    print("\n=== REGISTRAR USUARIO ===")
    nombre = input("Nombre completo: ")
    username = input("Nombre de usuario: ")
    email = input("Email: ")

    while True:
        password = input("Contraseña: ")
        confirmar = input("Confirmar contraseña: ")
        if password == confirmar:
            break
        print(" Las contraseñas no coinciden. Intente nuevamente.")

    u = Usuario(None, nombre, username, email, password)
    dao.registrar_usuario(u)
    print(" Usuario registrado correctamente.\n")

def login():
    print("\n===== INICIO DE SESIÓN =====")
    username = input("Usuario: ")
    password = input("Contraseña: ")

    usuario = dao.iniciar_sesion(username, password)

    if usuario:
        print(" Inicio de sesión correcto.\n")
        return True
    else:
        print(" Usuario o contraseña incorrectos.\n")
        return False

def menu_login():
    while True:
        print("===== LOGIN =====")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            if login():
                return True
        elif opcion == "3":
            print("Saliendo...")
            return False
        else:
            print("Opción inválida.")

# ===================================================
#  FUNCIONES AUXILIARES
# ===================================================
def pedir_fecha_valida():
    while True:
        fecha = input("Fecha (AAAA-MM-DD o vacío si no aplica): ").strip()
        if fecha == "":
            return None
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print(" Formato incorrecto. Usa AAAA-MM-DD.")

def pedir_float(mensaje):
    valor = input(mensaje).strip()
    if valor == "":
        return None
    try:
        return float(valor)
    except ValueError:
        print(" Valor inválido, se asignará 0.")
        return 0.0

def pedir_int(mensaje):
    valor = input(mensaje).strip()
    if valor == "":
        return None
    try:
        return int(valor)
    except ValueError:
        print(" Valor inválido, se asignará 0.")
        return 0

# ===================================================
# EMPLEADOS
# ===================================================
def registrar_empleado():
    print("\n=== REGISTRAR EMPLEADO ===")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    fecha_inicio = pedir_fecha_valida()
    salario = pedir_float("Salario: ")
    id_depto = pedir_int("ID Departamento: ")

    departamento = dao.obtener_departamento_por_id(id_depto)

    if not departamento:
        print("\n❌ No hay departamentos con ese ID.\n")
        return

    e = Empleado(None, nombre, direccion, telefono, email, fecha_inicio, salario, id_depto)
    dao.insertar_empleado(e)
    print(" Empleado registrado correctamente.")

def mostrar_empleados():
    print("\n=== LISTA DE EMPLEADOS ===")
    empleados = dao.obtener_empleados()

    for e in empleados:
        print(f"ID: {e[0]}")
        print(f"Nombre: {e[1]}")
        print(f"Dirección: {e[2]}")
        print(f"Teléfono: {e[3]}")
        print(f"Email: {e[4]}")
        print(f"Fecha inicio: {e[5]}")
        print(f"Salario: {e[6]}")
        print(f"ID Departamento: {e[7]}")
        print("-" * 40)

# ===================================================
# DEPARTAMENTOS
# ===================================================
def registrar_departamento():
    print("\n=== REGISTRAR DEPARTAMENTO ===")
    nombre = input("Nombre: ")
    gerente = input("Gerente: ")
    d = Departamento(None, nombre, gerente)
    dao.insertar_departamento(d)
    print(" Departamento registrado correctamente.")

def mostrar_departamentos():
    print("\n=== LISTA DE DEPARTAMENTOS ===")
    departamentos = dao.obtener_departamentos()

    for d in departamentos:
        print(f"ID: {d[0]}")
        print(f"Nombre: {d[1]}")
        print(f"Gerente: {d[2]}")
        print("-" * 40)

# ===================================================
# PROYECTOS
# ===================================================
def registrar_proyecto():
    print("\n=== REGISTRAR PROYECTO ===")
    nombre = input("Nombre del proyecto: ")
    descripcion = input("Descripción: ")
    fecha_inicio = pedir_fecha_valida()

    p = Proyecto(None, nombre, descripcion, fecha_inicio)
    dao.insertar_proyecto(p)
    print(" Proyecto registrado correctamente.")

def mostrar_proyectos():
    print("\n=== LISTA DE PROYECTOS ===")
    proyectos = dao.obtener_proyectos()

    for p in proyectos:
        print(f"ID: {p[0]}")
        print(f"Nombre: {p[1]}")
        print(f"Descripción: {p[2]}")
        print(f"Fecha inicio: {p[3]}")
        print("-" * 40)

# ===================================================
# MENÚ PRINCIPAL
# ===================================================
def menu_principal():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Agregar empleado")
        print("2. Mostrar empleados")
        print("3. Agregar departamento")
        print("4. Mostrar departamentos")
        print("5. Registrar proyecto")
        print("6. Mostrar proyectos")
        print("7. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            mostrar_empleados()
        elif opcion == "3":
            registrar_departamento()
        elif opcion == "4":
            mostrar_departamentos()
        elif opcion == "5":
            registrar_proyecto()
        elif opcion == "6":
            mostrar_proyectos()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# ===================================================
# PROGRAMA PRINCIPAL
# ===================================================
if menu_login():
    menu_principal()
