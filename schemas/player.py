from pydantic import BaseModel


class PlayerSchema(BaseModel):
    id: int
    money: int

class MessageSchema(BaseModel):
    message: str
    customer_id: int