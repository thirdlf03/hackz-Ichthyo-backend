class Chat(Base):
    __tablename__ = "chat"

    id = Colmn(Integer,primary_key=True)
    player_id = Column(Interger,ForeignKey("player.id"))
    customer_id = Colmn(Interger,Foreignkey("player.id"))
    message = Colmn(String(1024))