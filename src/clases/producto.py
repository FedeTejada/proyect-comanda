class Producto():
    def __init__(self, nombre, precio) -> None:
        self._nombre = nombre
        self._precio = precio

    # def set_nombre(self, nombre):
    #   self._nombre = nombre

    def set_precio(self, precio):
        self._precio = precio