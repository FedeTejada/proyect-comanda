from sqlalchemy import Column, Integer, String, DateTime, Boolean, Time, Null
from .Base import Base

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False)
    name_client = Column(String(255), nullable=False)
    delivery = Column(Boolean, nullable=False, default=False)
    ready_time = Column(Time, nullable=True, default=None)
    canceled = Column(Boolean, nullable=False, default=False)
    address = Column(String(255), nullable=True) 
    
    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_date(self):
        return self.date

    def set_date(self, value):
        self.date = value
    
    def get_name_client(self):
        return self.name_client

    def set_name_client(self, value):
        self.name_client = value

    def get_delivery(self):
        return self.delivery

    def set_delivery(self, value):
        self.delivery = value
        
    def get_ready_time(self):
        return self.ready_time

    def set_ready_time(self, value):
        self.ready_time = value

    def get_canceled(self):
        return self.canceled

    def set_canceled(self, value):
        self.canceled = value

    def get_address(self):
        return self.address

    def set_address(self, value):
        self.address = value
    
    def __str__(self):
        order_str = f"Order ID: {self.id}\nDate: {self.date}\nClient Name: {self.name_client}\nDelivery: {self.delivery}\nReady Time: {self.ready_time}\nCanceled: {self.canceled}\nAddress: {self.address}\n"
        return order_str
    
    def __hash__(self):
        return hash((self.id, self.date, self.name_client, self.delivery, self.ready_time, self.canceled, self.address))
    
    def __eq__(self, other):
        if not isinstance(other, Order):
            return False
        return self.__dict__ == other.__dict__