from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models.player import Player

router = APIRouter()

@router.get("/player")
def get_player(db: Session = Depends(get_db)):
    players = db.query(Player).all()
    return players