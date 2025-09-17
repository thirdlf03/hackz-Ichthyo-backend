from pydantic import BaseModel
from typing import Optional


class ChatSchema(BaseModel):
    id: int
    player_id: Optional[int] = None
    customer_id: Optional[int] = None
    message: Optional[str] = None

