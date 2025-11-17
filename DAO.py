import mysql.connector
from key import key
from Empleado import Empleado
from Departamento import Departamento
from Proyecto import Proyecto
from Usuario import Usuario
from decimal import Decimal

class DAO:
    def __init__(self):
        self.conn = None
        self.cursor = None

    # ========================
    # CONEXIÓN
    # ========================
    def conectar(self):
        self.conn = mysql.connector.connect(
            host=key["host"],
            user=key["user"],
            password=key["password"],
            database=key["db"]
        )
        self.cursor = self.conn.cursor()

    def desconectar(self):
        if self.cursor:
            try:
                self.cursor.fetchall()  # limpia resultados pendientes
            except:
                pass
            self.cursor.close()

        if self.conn:
            self.conn.close()

    # ========================
    # USUARIOS
    # ========================
    def registrar_usuario(self, usuario):
        self.conectar()
        sql = """INSERT INTO usuario (nombre, username, email, password)
                 VALUES (%s, %s, %s, %s)"""
        datos = (
            usuario.get_nombre(),
            usuario.get_username(),
            usuario.get_email(),
            usuario.get_password()
        )
        self.cursor.execute(sql, datos)
        self.conn.commit()
        self.desconectar()

    def iniciar_sesion(self, username, password):
        self.conectar()
        sql = "SELECT * FROM usuario WHERE username = %s AND password = %s"
        self.cursor.execute(sql, (username, password))

        usuario = self.cursor.fetchone()  # muy importante

        self.desconectar()
        return usuario

    # ========================
    # EMPLEADOS
    # ========================
    def insertar_empleado(self, empleado):
        self.conectar()
        sql = """INSERT INTO empleado (nombre, direccion, telefono, email,
                                       fecha_inicio, salario, iddepartamento)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        datos = (
            empleado.get_nombre(),
            empleado.get_direccion(),
            empleado.get_telefono(),
            empleado.get_email(),
            empleado.get_fecha_inicio(),
            empleado.get_salario(),
            empleado.get_iddepartamento()
        )

        self.cursor.execute(sql, datos)
        self.conn.commit()
        self.desconectar()

    def obtener_empleados(self):
        self.conectar()
        self.cursor.execute("SELECT * FROM empleado")
        resultados = self.cursor.fetchall()
        self.desconectar()
        return resultados

    # ========================
    # DEPARTAMENTOS
    # ========================
    def insertar_departamento(self, departamento):
        self.conectar()
        sql = "INSERT INTO departamento (nombre, gerente) VALUES (%s, %s)"
        datos = (departamento.get_nombre(), departamento.get_gerente())
        self.cursor.execute(sql, datos)
        self.conn.commit()
        self.desconectar()

    def obtener_departamentos(self):
        self.conectar()
        self.cursor.execute("SELECT * FROM departamento")
        resultados = self.cursor.fetchall()
        self.desconectar()
        return resultados

    # ⭐⭐⭐ NUEVA FUNCIÓN PARA VALIDAR DEPARTAMENTO ⭐⭐⭐
    def obtener_departamento_por_id(self, iddepto):
        self.conectar()
        sql = "SELECT * FROM departamento WHERE iddepartamento = %s"
        self.cursor.execute(sql, (iddepto,))
        resultado = self.cursor.fetchone()
        self.desconectar()
        return resultado

    # ========================
    # PROYECTOS
    # ========================
    def insertar_proyecto(self, proyecto):
        self.conectar()
        sql = """INSERT INTO proyecto (nombre, descripcion, fecha_inicio)
                 VALUES (%s, %s, %s)"""
        datos = (
            proyecto.get_nombre(),
            proyecto.get_descripcion(),
            proyecto.get_fecha_inicio()
        )
        self.cursor.execute(sql, datos)
        self.conn.commit()
        self.desconectar()

    def obtener_proyectos(self):
        self.conectar()
        self.cursor.execute("SELECT * FROM proyecto")
        resultados = self.cursor.fetchall()
        self.desconectar()
        return resultados
