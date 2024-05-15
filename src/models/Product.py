# Create of the class Products
class Product:
    def __init__(self,id,name,price):
        self._id = id
        self._name = name
        self._price = price

    def getName(self):
        return self._name
    
    def getPrice(self):
        return self._price
    
    def getCategory(self):
        return self._category
    
    def setName(self,name):
        self._name = name

    def setPrice(self,price):
        self._price = price


