from pydantic import BaseModel

class Player(BaseModel):
    id: int
    money: int