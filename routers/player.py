from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models.player import Player
from schemas.player import PlayerSchema

router = APIRouter()


@router.get("/player") 
def get_db(db: Session = Depends(get_db)):
    return db.query(Player).all()

@router.post("/player")
def create_player(player: PlayerSchema, db: Session= Depends(get_db)):
    new_db = Player(id = Player.id, money = Player.money)
    db.add(new_db)
    db.commit()
    return db.query(Player).all()

@router.put("/player/money")
async def update_money(player_id: int, player: PlayerSchema, db: Session = Depends(get_db)):
    player_update_money = player_money + service_money

    return db.query(Player).all()