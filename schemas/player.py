from pydantic import BaseModel


class PlayerSchema(BaseModel):
    id: int
    money: int
