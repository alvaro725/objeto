import mysql.connector
from key import key
from Empleado import Empleado
from Departamento import Departamento
from Proyecto import Proyecto

class DAO:
    def __init__(self):
        self.conn = None
        self.cursor = None

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
            self.cursor.close()
        if self.conn:
            self.conn.close()

    # 🔹 EMPLEADOS CRUD
    def insertar_empleado(self, empleado):
        self.conectar()
        sql = """INSERT INTO empleado (nombre, direccion, telefono, email, fecha_inicio, salario, id_departamento)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        datos = (empleado.get_nombre(), empleado.get_direccion(), empleado.get_telefono(),
                 empleado.get_email(), empleado.get_fecha_inicio(), empleado.get_salario(),
                 empleado.get_id_departamento())
        self.cursor.execute(sql, datos)
        self.conn.commit()
        self.desconectar()

    def obtener_empleados(self):
        self.conectar()
        self.cursor.execute("SELECT * FROM empleado")
        resultados = self.cursor.fetchall()
        self.desconectar()
        return resultados

    def eliminar_empleado(self, id_empleado):
        self.conectar()
        self.cursor.execute("DELETE FROM empleado WHERE idempleado = %s", (id_empleado,))
        self.conn.commit()
        self.desconectar()

    # 🔹 DEPARTAMENTOS CRUD
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

    def insertar_proyecto(self, proyecto):
        self.conectar()
        sql = """INSERT INTO proyecto (nombre, descripcion, fecha_inicio)
                 VALUES (%s, %s, %s)"""
        datos = (proyecto.get_nombre(), proyecto.get_descripcion(), proyecto.get_fecha_inicio())
        self.cursor.execute(sql, datos)
        self.conn.commit()
        self.desconectar()

    def obtener_proyectos(self):
        self.conectar()
        self.cursor.execute("SELECT * FROM proyecto")
        resultados = self.cursor.fetchall()
        self.desconectar()
        return resultados

    def eliminar_proyecto(self, id_proyecto):
        self.conectar()
        self.cursor.execute("DELETE FROM proyecto WHERE idproyecto = %s", (id_proyecto,))
        self.conn.commit()
        self.desconectar()
