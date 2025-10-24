import mysql.connector
from key import key

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

    # Insertar empleado (ID se asigna automáticamente en la base de datos)
    def insertar_empleado(self, empleado):
        self.conectar()
        sql = """
        INSERT INTO empleado (nombre, direccion, telefono, email, fecha_inicio, salario, id_departamento)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        datos = (
            empleado.nombre,
            empleado.direccion,
            empleado.telefono,
            empleado.email,
            empleado.fecha_inicio,
            empleado.salario,
            empleado.id_departamento
        )
        self.cursor.execute(sql, datos)
        self.conn.commit()
        self.desconectar()

    # Obtener todos los empleados
    def obtener_empleados(self):
        self.conectar()
        self.cursor.execute("SELECT * FROM empleado")
        resultados = self.cursor.fetchall()
        self.desconectar()
        return resultados

    # Insertar departamento (ID automático)
    def insertar_departamento(self, departamento):
        self.conectar()
        sql = "INSERT INTO departamento (nombre, gerente) VALUES (%s, %s)"
        datos = (departamento.nombre, departamento.gerente)
        self.cursor.execute(sql, datos)
        self.conn.commit()
        self.desconectar()

    # Obtener todos los departamentos
    def obtener_departamentos(self):
        self.conectar()
        self.cursor.execute("SELECT * FROM departamento")
        resultados = self.cursor.fetchall()
        self.desconectar()
        return resultados

    # Actualizar empleado
    def actualizar_empleado(self, empleado):
        self.conectar()
        sql = """
        UPDATE empleado SET nombre=%s, direccion=%s, telefono=%s, email=%s, fecha_inicio=%s, salario=%s, id_departamento=%s
        WHERE id_empleado=%s
        """
        datos = (
            empleado.nombre,
            empleado.direccion,
            empleado.telefono,
            empleado.email,
            empleado.fecha_inicio,
            empleado.salario,
            empleado.id_departamento,
            empleado.id_empleado
        )
        self.cursor.execute(sql, datos)
        self.conn.commit()
        self.desconectar()

    # Eliminar empleado
    def eliminar_empleado(self, id_empleado):
        self.conectar()
        sql = "DELETE FROM empleado WHERE id_empleado = %s"
        self.cursor.execute(sql, (id_empleado,))
        self.conn.commit()
        self.desconectar()

    # Actualizar departamento
    def actualizar_departamento(self, departamento):
        self.conectar()
        sql = "UPDATE departamento SET nombre=%s, gerente=%s WHERE id_departamento=%s"
        datos = (departamento.nombre, departamento.gerente, departamento.id_departamento)
        self.cursor.execute(sql, datos)
        self.conn.commit()
        self.desconectar()

    # Eliminar departamento
    def eliminar_departamento(self, id_departamento):
        self.conectar()
        sql = "DELETE FROM departamento WHERE id_departamento = %s"
        self.cursor.execute(sql, (id_departamento,))
        self.conn.commit()
        self.desconectar()
