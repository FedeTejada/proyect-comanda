from src.models.Order import Order
from src.models.OrderProduct import OrderProduct
from src.models.Product import Product
from src.config.config import session
import datetime

db = session

def create_order(delivery=bool, name_client=str, ready_time=any,address=any):
    if (delivery==False):
        datanow = datetime.datetime.now()
        newOrder = Order(date = datanow, name_client=name_client, delivery = delivery)
    else:
        newOrder = Order(date = datetime.datetime.now(), name_client=name_client, ready_time=ready_time, delivery=delivery, address=address)
    db.add(newOrder)
    db.flush()
    return newOrder

def save_order(order=Order):
    db.commit()
    db.refresh(order)

def cancel_order(order=Order):
    order = db.query(Order).filter(Order.id==order.id).first()
    if order:
        order.canceled=True
    db.commit()
    db.refresh(order)

def mod_order(order=Order, address=str, customer=str, ready_time=datetime, observation=str, cadete=bool):
    # control? observation falta.
    if cadete:
        order.set_delivery(cadete)
    if address:
        order.set_address(address)
    if ready_time:
        order.set_ready_time(ready_time)
    if customer:
        order.set_name_client(customer)
    
    return order