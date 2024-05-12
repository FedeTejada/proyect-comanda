class Producto():
    def __init__(self, nombre, precio, categoria) -> None:
        self._nombre = nombre
        self._precio = precio
        self._categoria = categoria

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_precio(self, precio):
        self._precio = precio
    
    def set_categoria(self, categoria):
        self._categoria = categoria
    