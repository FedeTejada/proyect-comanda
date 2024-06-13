from models.Product import Product


def addProducts():
    name = input("Add new name product")
    price = int(input("insert new price of the product"))
    newProduct= Product(1,name,price)

def deleteProduct():
    