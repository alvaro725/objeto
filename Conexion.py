import mysql.connector

class Conexion:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='123456',
                database='mydb'
            )
            self.cursor = self.conexion.cursor()
            print("Conexión establecida correctamente")
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")

    def ejecutar_consulta(self, consulta, params=None):
        """
        Ejecuta una consulta SELECT y devuelve los resultados.
        :param consulta: string con la consulta SQL.
        :param params: tupla con parámetros para la consulta (opcional).
        :return: lista con los resultados.
        """
        try:
            self.cursor.execute(consulta, params)
            resultados = self.cursor.fetchall()
            return resultados
        except mysql.connector.Error as err:
            print(f"Error al ejecutar consulta: {err}")
            return None

    def ejecutar_sentencia(self, sentencia, params=None):
        """
        Ejecuta una sentencia INSERT, UPDATE o DELETE.
        :param sentencia: string con la sentencia SQL.
        :param params: tupla con parámetros para la sentencia (opcional).
        :return: True si tuvo éxito, False si hubo error.
        """
        try:
            self.cursor.execute(sentencia, params)
            self.conexion.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al ejecutar sentencia: {err}")
            return False

    def cerrar(self):
        """
        Cierra la conexión y el cursor.
        """
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
        print("Conexión cerrada")
