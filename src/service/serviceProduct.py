from models.Product import Product
from config.config import engine,session
import logging
logger = logging.getLogger(__name__)

db = session
# Service of the product, add update delete products

def addProducts(name,price):
    newProduct= Product(name=name , price=price)
    db.add(newProduct)
    db.commit()
    db.refresh(newProduct)

def getAllProducts():
    return db.query(Product).all()


def updateProduct(product_id, name=None, price=None):
    product = db.query(Product).filter(Product.id == product_id).first()
    # Verify what product is not null 
    if product != None:
        if product:
            if name:
                product.name = name
            if price:
                product.price = price
        db.commit()
        db.refresh(product)
    else: #if the product is NULL, shows mensagge the error
        print("El producto con el ID seleccionado no se encunetra en la base de datos")
    #print(type(product)) 

# 
def deleteProduct(product_id):
    #find product for id whith product_id
    product = db.query(Product).filter(Product.id == product_id).first() #if we found the product 
    print(type(product))
    #if the product exist is delete.
    if product != None:
        if product:
            db.delete(product)
            db.commit()
    else:
        print("No se encontro el producto a eliminar.")
        
def get_product_id_by_name(product_name):
    product = db.query(Product).filter_by(name=product_name).first()
    return product.id if product else None