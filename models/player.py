class Player(Base):
    __tablename__ = "player"

    id = column(Interger, primary_key=True)
    money = Column(Interger)  
