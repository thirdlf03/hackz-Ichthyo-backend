from ..db import Base
from sqlalchemy import Column, Integer

class Player(Base):
    __tablename__ = "player"

    id = Column(Integer, primary_key=True)
    money = Column(Integer)  
