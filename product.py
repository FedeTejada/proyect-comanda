class Product:
    def __init__(self, name , cant, price):
        self._name = name
        self._cant = cant
        self._price = price

    def set_Name(self, name):
        self._name = name

    def set_Name(self, cant):
        self._cant = cant

    def set_Name(self, price):
        self._price = price

    def get_Name(self):
        return self._name
    
    def get_Cant(self):
        return self._cant

    def get_Price(self):
        return self._price