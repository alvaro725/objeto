import mysql.connector
from mysql.connector import Error

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

    # Getters y setters
    def get_idempleado(self):
        return self.__idempleado
    def set_idempleado(self, idempleado):
        self.__idempleado = idempleado

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_direccion(self):
        return self.__direccion
    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_telefono(self):
        return self.__telefono
    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    def get_fecha_inicio(self):
        return self.__fecha_inicio
    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def get_salario(self):
        return self.__salario
    def set_salario(self, salario):
        self.__salario = salario

    def get_id_departamento(self):
        return self.__id_departamento
    def set_id_departamento(self, id_departamento):
        self.__id_departamento = id_departamento

    def __str__(self):
        return f"ID: {self.__idempleado}\nNombre: {self.__nombre}\nDirección: {self.__direccion}\nTeléfono: {self.__telefono}\nEmail: {self.__email}\nFecha Inicio: {self.__fecha_inicio}\nSalario: {self.__salario}\nID Departamento: {self.__id_departamento}"


class EmpleadoDAO:
    def __init__(self, host, user, password, database):
        self.conn = None
        self.cursor = None
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            # print("Conexión exitosa")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        # print("Conexión cerrada")

    def insertar_empleado(self, empleado: Empleado):
        try:
            self.conectar()
            sql = """
                INSERT INTO empleado (nombre, direccion, telefono, email, fecha_inicio, salario, id_departamento)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            datos = (
                empleado.get_nombre(),
                empleado.get_direccion(),
                empleado.get_telefono(),
                empleado.get_email(),
                empleado.get_fecha_inicio(),
                empleado.get_salario(),
                empleado.get_id_departamento()
            )
            self.cursor.execute(sql, datos)
            self.conn.commit()
            empleado_id = self.cursor.lastrowid
            return empleado_id
        except Error as e:
            print(f"Error al insertar empleado: {e}")
            return None
        finally:
            self.desconectar()

    def obtener_empleado_por_id(self, idempleado):
        try:
            self.conectar()
            sql = "SELECT * FROM empleado WHERE idempleado = %s"
            self.cursor.execute(sql, (idempleado,))
            row = self.cursor.fetchone()
            if row:
                empleado = Empleado(
                    idempleado=row[0],
                    nombre=row[1],
                    direccion=row[2],
                    telefono=row[3],
                    email=row[4],
                    fecha_inicio=row[5],
                    salario=row[6],
                    id_departamento=row[7]
                )
                return empleado
            else:
                return None
        except Error as e:
            print(f"Error al obtener empleado: {e}")
            return None
        finally:
            self.desconectar()

    def actualizar_empleado(self, empleado: Empleado):
        try:
            self.conectar()
            sql = """
                UPDATE empleado
                SET nombre=%s, direccion=%s, telefono=%s, email=%s, fecha_inicio=%s, salario=%s, id_departamento=%s
                WHERE idempleado=%s
            """
            datos = (
                empleado.get_nombre(),
                empleado.get_direccion(),
                empleado.get_telefono(),
                empleado.get_email(),
                empleado.get_fecha_inicio(),
                empleado.get_salario(),
                empleado.get_id_departamento(),
                empleado.get_idempleado()
            )
            self.cursor.execute(sql, datos)
            self.conn.commit()
            return self.cursor.rowcount  # Número de filas afectadas
        except Error as e:
            print(f"Error al actualizar empleado: {e}")
            return 0
        finally:
            self.desconectar()

    def eliminar_empleado(self, idempleado):
        try:
            self.conectar()
            sql = "DELETE FROM empleado WHERE idempleado = %s"
            self.cursor.execute(sql, (idempleado,))
            self.conn.commit()
            return self.cursor.rowcount
        except Error as e:
            print(f"Error al eliminar empleado: {e}")
            return 0
        finally:
            self.desconectar()

    def listar_empleados(self):
        try:
            self.conectar()
            sql = "SELECT * FROM empleado"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            empleados = []
            for row in rows:
                empleado = Empleado(
                    idempleado=row[0],
                    nombre=row[1],
                    direccion=row[2],
                    telefono=row[3],
                    email=row[4],
                    fecha_inicio=row[5],
                    salario=row[6],
                    id_departamento=row[7]
                )
                empleados.append(empleado)
            return empleados
        except Error as e:
            print(f"Error al listar empleados: {e}")
            return []
        finally:
            self.desconectar()
