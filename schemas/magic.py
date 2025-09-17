from pydantic import BaseModel
from typing import Optional


class MagicSchema(BaseModel):
    id: int
    magic_name: str
    effect: Optional[str] = None

