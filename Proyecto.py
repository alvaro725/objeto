class Proyecto:
    def __init__(self,id_proyecto, nombre, descripcion, fecha_inicio):
        self.__id_proyecto = id_proyecto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio

    def get_id_proyecto(self):
        return self.__id_proyecto
    def set_id_proyecto(self,id_proyecto):
        self.__id_proyecto = id_proyecto

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre

    def get_descripcion(self):
        return self.__descripcion
    def set_descripcion(self,descripcion):
        self.__descripcion = descripcion
    
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    def set_fecha_inicio(self,fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def crear(self):
        print(f"Proyecto '{self.__nombre}' creado correctamente")

    def leer(self):
        print(f"Informacion del proyecto: \n{self}")
    
    def actualizar(self,nombre, descripcion, fecha_inicio):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha_inicio
        print(f"Proyecto '{self.__id}' actualizado correctamente")