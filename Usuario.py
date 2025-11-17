class Usuario:
    def __init__(self, idusuario=None, nombre=None, username=None, email=None, password=None):
        self.__idusuario = idusuario
        self.__nombre = nombre
        self.__username = username
        self.__email = email
        self.__password = password

    # GETTERS
    def get_idusuario(self): return self.__idusuario
    def get_nombre(self): return self.__nombre
    def get_username(self): return self.__username
    def get_email(self): return self.__email
    def get_password(self): return self.__password

    # SETTERS
    def set_idusuario(self, v): self.__idusuario = v
    def set_nombre(self, v): self.__nombre = v
    def set_username(self, v): self.__username = v
    def set_email(self, v): self.__email = v
    def set_password(self, v): self.__password = v

    def __str__(self):
        return f"Usuario[ID={self.__idusuario}, Username={self.__username}]"
