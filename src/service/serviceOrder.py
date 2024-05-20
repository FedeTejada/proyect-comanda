from models.Order import Order
from models.OrderProduct import OrderProduct
from models.Product import Product
from config.config import session
import datetime

db = session

def createOrder(delivery=bool, name_client=str):
    newOrder = Order(date = datetime.datetime.now(),name_client=name_client, delivery=delivery)
    db.add(newOrder)
    db.commit()
    db.refresh(newOrder)
    
def addProductToOrder(producto_id=int, order_id=int ,quantity=int):
    order_product = db.query(OrderProduct).filter(OrderProduct.order_id == order_id and OrderProduct.product_id==producto_id).first()
    if order_product:
        modOrder(order_id, producto_id, quantity)
    else:
        newOrderProduct = OrderProduct(product_id=producto_id, order_id=order_id, cantidad=quantity)
        db.add(newOrderProduct)
        db.commit()
        db.refresh(newOrderProduct)

def cancelOrder(order=Order):
    order = db.query(Order).filter(Order.id==order.id).first()
    if order:
        order.canceled=True
    db.commit()
    db.refresh(order)

def modOrder(idOrder=int, idProduct=int, quantity=int):
    order_product = db.query(OrderProduct).filter(OrderProduct.order_id == idOrder and OrderProduct.product_id==idProduct).first()
    if order_product:
        order_product.cantidad += quantity
    db.commit()
    db.refresh(order_product)