from sqlalchemy import *
from sqlalchemy.orm import relationship

from python.database.Base import Base


class Order(Base):
    __tablename__ = "orders"
    order_date = Column(Date)
    delivery_date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"))
    receive_code = Column(
        Integer,
        Sequence('receive_code_seq'),
        default=Sequence('receive_code_seq').next_value(),
        unique=True
        )
    status = Column(String)
    pickup_point_code = Column(Integer, ForeignKey("pick-up_points.id"))
    order_number = Column(Integer, primary_key=True, autoincrement=True)

    order_items = relationship(
        'OrderItem',
        back_populates='order',
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    user = relationship('User', back_populates='orders')
    pickup_point = relationship('PickupPoint', back_populates='orders')