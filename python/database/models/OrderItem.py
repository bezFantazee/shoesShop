from sqlalchemy import *
from sqlalchemy.orm import relationship

from python.database.Base import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    order_number = Column(Integer, ForeignKey("orders.order_number"), primary_key=True)
    shoe_id = Column(Integer, ForeignKey("shoes.id"), primary_key=True)
    order = relationship('Order', back_populates='order_items')
    shoes = relationship('Shoe', back_populates='order_items')
    quantity = Column(SmallInteger)