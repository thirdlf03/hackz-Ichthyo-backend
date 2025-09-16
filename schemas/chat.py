from pydantic import BaseModel
from typing import Optional

class Chat(BaseModel):
    id: int
    player_id: int
    customer_id: int
    effect: Optional[str] = None