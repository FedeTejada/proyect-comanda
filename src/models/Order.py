from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .Base import Base

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False)
    name_client = Column(String(255), nullable=False)
    delivery = Column(Boolean, nullable=False, default=False)
    canceled = Column(Boolean, nullable=False, default=False)