from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Chat(Base):
    __tablename__ = "chat"

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("player.id"))
    customer_id = Column(Integer, ForeignKey("customer.id"))
    message = Column(String(1024))

