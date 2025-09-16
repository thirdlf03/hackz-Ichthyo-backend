from pydantic import BaseModel
from typing import Optional

class Customer(BaseModel):
    id: int
    name: str
    money: int = 0
    profile: Optional[str] = None
    level: int = 1
    status: str = "active"
    age: Optional[int] = None