class Departamento:
    def __init__(self, iddepartamento=None, nombre=None, gerente=None):
        self.__iddepartamento = iddepartamento
        self.__nombre = nombre
        self.__gerente = gerente

    # GETTERS
    def get_iddepartamento(self):
        return self.__iddepartamento

    def get_nombre(self):
        return self.__nombre

    def get_gerente(self):
        return self.__gerente

    # SETTERS
    def set_iddepartamento(self, iddepartamento):
        self.__iddepartamento = iddepartamento

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_gerente(self, gerente):
        self.__gerente = gerente

    def __str__(self):
        return f"Departamento [ID={self.__iddepartamento}, Nombre={self.__nombre}, Gerente={self.__gerente}]"
