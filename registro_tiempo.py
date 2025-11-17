class RegistroTiempo:
    def __init__(self, idregistro=None, idempleado=None, idproyecto=None, fecha=None, horas=None):
        self.__idregistro = idregistro
        self.__idempleado = idempleado
        self.__idproyecto = idproyecto
        self.__fecha = fecha
        self.__horas = horas

    def get_idregistro(self): return self.__idregistro
    def set_idregistro(self, idregistro): self.__idregistro = idregistro

    def get_idempleado(self): return self.__idempleado
    def set_idempleado(self, idempleado): self.__idempleado = idempleado

    def get_idproyecto(self): return self.__idproyecto
    def set_idproyecto(self, idproyecto): self.__idproyecto = idproyecto

    def get_fecha(self): return self.__fecha
    def set_fecha(self, fecha): self.__fecha = fecha

    def get_horas(self): return self.__horas
    def set_horas(self, horas): self.__horas = horas

    def __str__(self):
        return f"RegistroTiempo [ID={self.__idregistro}, Emp={self.__idempleado}, Proy={self.__idproyecto}, Horas={self.__horas}]"
