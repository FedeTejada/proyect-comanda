import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from models import Base, Product, Order, OrderProduct
from config import engine

def create_tables():
    Base.metadata.create_all(engine)
    
def main():
    create_tables()
    
if __name__ == "__main__":
    main()
