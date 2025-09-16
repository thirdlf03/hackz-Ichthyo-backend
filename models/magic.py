class Magic(Base):
    __tablename__ = "magic"

    id = Column(Interger,primary_key=True)
    magic_name = Column(String(1024))
    effect = Column(String(1024))