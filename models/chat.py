class Chat(Base):
    __tablename__ = "chat"

    id = Column(Integer,primary_key=True)
    player_id = Column(Interger,ForeignKey("player.id"))
    customer_id = Column(Interger,ForeignKey("customer.id"))
    message = Column(String(1024))