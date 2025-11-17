class Proyecto:
    def __init__(self, idproyecto=None, nombre=None, descripcion=None, fecha_inicio=None):
        self.__idproyecto = idproyecto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio

    def get_idproyecto(self): return self.__idproyecto
    def set_idproyecto(self, idproyecto): self.__idproyecto = idproyecto

    def get_nombre(self): return self.__nombre
    def set_nombre(self, nombre): self.__nombre = nombre

    def get_descripcion(self): return self.__descripcion
    def set_descripcion(self, descripcion): self.__descripcion = descripcion

    def get_fecha_inicio(self): return self.__fecha_inicio
    def set_fecha_inicio(self, fecha_inicio): self.__fecha_inicio = fecha_inicio

    def __str__(self):
        return f"Proyecto [ID={self.__idproyecto}, Nombre={self.__nombre}, Inicio={self.__fecha_inicio}]"
