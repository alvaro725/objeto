import re
from DAO import DAO
from Empleado import Empleado
from Departamento import Departamento
from Proyecto import Proyecto
from decimal import Decimal
from datetime import datetime

dao = DAO()

def pedir_fecha_valida():
    while True:
        fecha = input("Fecha (AAAA-MM-DD o vacío si no aplica): ").strip()
        if fecha == "":
            return None
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print(" Formato incorrecto. Usa AAAA-MM-DD (ejemplo: 2025-10-24)")

def pedir_float(mensaje):
    """Pide un número decimal o deja en None si hay error."""
    valor = input(mensaje).strip()
    if valor == "":
        return None
    try:
        return float(valor)
    except ValueError:
        print(" Valor inválido, se asignará 0 por defecto.")
        return 0.0

def pedir_int(mensaje):
    """Pide un entero o deja en None si hay error."""
    valor = input(mensaje).strip()
    if valor == "":
        return None
    try:
        return int(valor)
    except ValueError:
        print(" Valor inválido, se asignará 0 por defecto.")
        return 0

def registrar_empleado():
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    fecha_inicio = pedir_fecha_valida()
    salario = pedir_float("Salario: ")
    id_depto = pedir_int("ID Departamento: ")
    
    e = Empleado(None, nombre, direccion, telefono, email, fecha_inicio, salario, id_depto)
    dao.insertar_empleado(e)
    print(" Empleado registrado correctamente.")

def mostrar_empleados():
    empleados = dao.obtener_empleados()
    for e in empleados:
        datos_limpios = []
        for valor in e:
            if valor is None:
                datos_limpios.append("")
            elif isinstance(valor, Decimal):
                datos_limpios.append(float(valor))
            else:
                datos_limpios.append(valor)
        print(tuple(datos_limpios))

def registrar_departamento():
    nombre = input("Nombre del departamento: ")
    gerente = input("Gerente: ")
    d = Departamento(None, nombre, gerente)
    dao.insertar_departamento(d)
    print(" Departamento registrado correctamente.")

def mostrar_departamentos():
    departamentos = dao.obtener_departamentos()
    for d in departamentos:
        datos_limpios = []
        for valor in d:
            if valor is None:
                datos_limpios.append("")
            elif isinstance(valor, Decimal):
                datos_limpios.append(float(valor))
            else:
                datos_limpios.append(valor)
        print(tuple(datos_limpios))

def registrar_proyecto():
    nombre = input("Nombre del proyecto: ")
    descripcion = input("Descripción: ")
    fecha_inicio = pedir_fecha_valida()
    p = Proyecto(None, nombre, descripcion, fecha_inicio)
    dao.insertar_proyecto(p)
    print(" Proyecto registrado correctamente.")

def mostrar_proyectos():
    proyectos = dao.obtener_proyectos()
    for p in proyectos:
        datos_limpios = []
        for valor in p:
            if valor is None:
                datos_limpios.append("")
            elif isinstance(valor, Decimal):
                datos_limpios.append(float(valor))
            else:
                datos_limpios.append(valor)
        print(tuple(datos_limpios))

def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Registrar Empleado")
        print("2. Mostrar Empleados")
        print("3. Registrar Departamento")
        print("4. Mostrar Departamentos")
        print("5. Registrar Proyecto")
        print("6. Mostrar Proyectos")
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
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")

menu()
#prueba