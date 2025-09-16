class Customer(Base):
    __tablename__ = "customer"

    id = Column(Interger,primay_key=True)
    name = Column(String(1024))
    money = Column(Integer)
    profile = Column(String(1024))
    level = Column(Integer)
    status = Column(String(1024))


