from sqlalchemy import *
from sqlalchemy.orm import relationship

from python.database.Base import Base


class PickupPoint(Base):
    __tablename__="pick-up_points"
    id = Column(Integer, primary_key=True)
    postal_code = Column(BigInteger)
    town = Column(String)
    street = Column(String)
    house = Column(String)

    orders = relationship('Order', back_populates='pickup_point')