#Crate of the class Orders
class Orders:
    def __init__(self,id,date,nameClient,delivery):
        self._date = date
        self._nameClient = nameClient
        self._delivery = delivery

    def getDate(self):
        return self._date
    
    def getNameClient(self):
        return self._nameClient
    
    def getDelivery(self):
        return self._delivery
    
    def setDate(self,date):
        self._date = date

    def setNameClient(self,nameClient):
        self._nameClient = nameClient

    def setDelivery(self,delivery):
        self._delivery = delivery

