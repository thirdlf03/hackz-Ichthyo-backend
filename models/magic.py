class Magic(Base):
    __tablename__ = "magic"

    id = Column(Interger,primary_key=True)
    magic_name = Colmn(String(1024))
    effect = Column(String(1024))