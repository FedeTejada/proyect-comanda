# models/order_product.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .Base import Base

class OrderProduct(Base):
    __tablename__ = 'order_product'
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    cantidad = Column(Integer, nullable=False)
    
    product = relationship('Product')
    order = relationship('Order')
