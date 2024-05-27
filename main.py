import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.models import Base, Product, Order, OrderProduct
from src.config import engine
from src.service.serviceProduct import addProducts
from src.service.serviceProduct import *
from src.service.change_products import frame_modif_product

def createTables():
    Base.metadata.create_all(engine)
    
def main():
    frame_modif_product()
    #name = input("Add new name product:\n")
    #price = int(input("insert new price of the product:\n"))
    #addProducts(name,price)
    
    
if __name__ == "__main__":
    main()
