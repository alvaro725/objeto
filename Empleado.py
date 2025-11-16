
class Empleado:
    def __init__(self, idempleado=None, nombre=None, direccion=None, telefono=None, email=None, fecha_inicio=None, salario=None, id_departamento=None):
        self.__idempleado = idempleado
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__fecha_inicio = fecha_inicio
        self.__salario = salario
        self.__id_departamento = id_departamento

    def get_idempleado(self): return self.__idempleado
    def set_idempleado(self, idempleado): self.__idempleado = idempleado

    def get_nombre(self): return self.__nombre
    def set_nombre(self, nombre): self.__nombre = nombre

    def get_direccion(self): return self.__direccion
    def set_direccion(self, direccion): self.__direccion = direccion

    def get_telefono(self): return self.__telefono
    def set_telefono(self, telefono): self.__telefono = telefono

    def get_email(self): return self.__email
    def set_email(self, email): self.__email = email

    def get_fecha_inicio(self): return self.__fecha_inicio
    def set_fecha_inicio(self, fecha_inicio): self.__fecha_inicio = fecha_inicio

    def get_salario(self): return self.__salario
    def set_salario(self, salario): self.__salario = salario

    def get_id_departamento(self): return self.__id_departamento
    def set_id_departamento(self, id_departamento): self.__id_departamento = id_departamento

    def __str__(self):
        return f"Empleado [ID={self.__idempleado}, Nombre={self.__nombre}, Email={self.__email}, Salario={self.__salario}]"
