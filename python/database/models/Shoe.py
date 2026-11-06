from sqlalchemy import *
from sqlalchemy.orm import relationship

from python.database.Base import Base

class Shoe(Base):
    __tablename__="shoes"
    id = Column(Integer, primary_key=True)
    article = Column(String, default="Не определен")
    name = Column(String, default="Не определен")
    unit = Column(String, default="Не определен")
    price = Column(Integer, default=0)
    supplier = Column(String, default="Не определен")
    manufacturer = Column(String, default="Не определен")
    category = Column(String, default="Не определен")
    discount = Column(SmallInteger, default=0)
    quantity_in_stock = Column(Integer, default=0)
    description = Column(Text, default="Не определен")
    image = Column(String, default="Не определен")

    order_items = relationship('OrderItem', back_populates='shoes')