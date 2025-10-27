import mysql.connector
from mysql.connector import Error
from key import key

class Conexion:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host=key["host"],
                user=key["user"],
                password=key["password"],
                database=key["db"]
            )
            self.cursor = self.conexion.cursor()
            print("Conexión establecida correctamente")
        except Error as err:
            print(f"Error al conectar a la base de datos: {err}")

    def ejecutar_consulta(self, consulta, params=None):
        try:
            self.cursor.execute(consulta, params)
            return self.cursor.fetchall()
        except Error as err:
            print(f"Error al ejecutar consulta: {err}")
            return None

    def ejecutar_sentencia(self, sentencia, params=None):
        try:
            self.cursor.execute(sentencia, params)
            self.conexion.commit()
            return True
        except Error as err:
            print(f"Error al ejecutar sentencia: {err}")
            return False

    def cerrar(self):
        if self.cursor: self.cursor.close()
        if self.conexion: self.conexion.close()
        print("Conexión cerrada")
