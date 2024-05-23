import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.models import Base, Product, Order, OrderProduct
from src.config import engine
from src.service.serviceProduct import addProducts
from src.service.serviceProduct import *


def createTables():
    Base.metadata.create_all(engine)
    
def main():
    #name = input("Add new name product:\n")
    #price = int(input("insert new price of the product:\n"))
    #addProducts(name,price)
    updateProduct(2,"pizza",800)
    
    
if __name__ == "__main__":
    main()
