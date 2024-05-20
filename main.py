import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from models import Base, Product, Order, OrderProduct
from config import engine
from service.serviceProduct import addProducts
from service.serviceProduct import *
from service.serviceOrder import *



def createTables():
    Base.metadata.create_all(engine)


def main():
    name = "Lomito"
    price = float(500.50)
    addProducts(name,price)
    name = "pizza"
    price = float(200.50)
    addProducts(name,price)
    
    createOrder(False,"chupachichi")
    addProductToOrder(1,4,1)
    addProductToOrder(1,4,2)
    
if __name__ == "__main__":
    main()
