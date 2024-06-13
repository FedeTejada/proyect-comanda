from sqlalchemy import Column, Integer, String, Float
from .Base import Base

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False,  unique=True)
    price = Column(Float, nullable=False)
    photo = Column(String(255), nullable=True)
