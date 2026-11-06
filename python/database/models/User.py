from python.database.Base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    patronymic = Column(String)
    login = Column(String)
    password = Column(String)
    status = Column(String)

    orders = relationship("Order", back_populates='user')

