from models.Order import Order
from models.OrderProduct import OrderProduct
from models.Product import Product
from config.config import session
import datetime

db = session

def add_product_order(product_id=int, order_id=int ,quantity=int):
    order_product = db.query(OrderProduct).filter(OrderProduct.order_id == order_id and OrderProduct.product_id==product_id).first()
    if order_product:
        mod_order_pro(order_id, product_id, quantity)
    else:
        newOrderProduct = OrderProduct(product_id=product_id, order_id=order_id, quantity=quantity)
        return newOrderProduct

def mod_order_pro(idOrder=int, idProduct=int, quantity=int):
    order_product = db.query(OrderProduct).filter(OrderProduct.order_id == idOrder and OrderProduct.product_id==idProduct).first()
    if order_product:
        order_product.quantity += quantity
    db.refresh(order_product)

def save_pro_ord(product_order):
    db.add(product_order)
    db.commit()
    db.refresh(product_order)

