from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from ..db import get_db
from ..models.player import Player

router = APIRouter()

@router.get("/player")
#playerから情報を持ってくる