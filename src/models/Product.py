# Create of the class Products
class Product:
    def __init__(self,id,name,amount,price,category):
        self._id = id
        self._name = name
        self._amount = amount
        self._price = price
        self._category = category

    def get_Name(self):
        return self._name
    
    def get_Amount(self):
        return self._amount
    
    def get_Name(self):
        return self._price
    
    def get_Amount(self):
        return self._category
    
    def set_Name(self,name):
        self._name = name

    def set_Name(self,amount):
        self._amount = amount

    def set_Name(self,price):
        self._price = price

    def set_Name(self,category):
        self._category = category

