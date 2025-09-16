from ..db import Base
from sqlalchemy import Column, Integer,String

class Magic(Base):
    __tablename__ = "magic"

    id = Column(Integer,primary_key=True)
    magic_name = Column(String(1024))
    effect = Column(String(1024))