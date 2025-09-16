from db import Base
from sqlalchemy import Column, Integer, String


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primay_key=True)
    name = Column(String(1024))
    money = Column(Integer)
    profile = Column(String(1024))
    level = Column(Integer)
    status = Column(String(1024))
    age = Column(Integer)
