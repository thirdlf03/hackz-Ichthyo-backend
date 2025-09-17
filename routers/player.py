from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, text
from db import get_db
from models.player import Player
from schemas.player import PlayerSchema

router = APIRouter()


@router.get("/player") 
async def get_player(db: Session = Depends(get_db)):
    sql = """
    SELECT * FROM player
    """

    result = await db.execute(text(sql))
    player = result.fetchone()

    return player._asdict()

@router.post("/player")
async def create_player(player: PlayerSchema, db: Session = Depends(get_db)):
    sql = """
    INSERT INTO player (id, money)
    VALUES (id, money)
    """

 
    await db.execute(text(sql), {"id": player.id, "money": player.money})
    await db.commit()

    sql_select = """
    SELECT * FROM player WHERE id = :id
    """
    result = await db.execute(text(sql_select), {"id": player.id,"money":player.money})
    new_player = result.fetchone()

    return dict(new_player._mapping) if new_player else None

@router.put("/player/money")
async def update_money(player: PlayerSchema, db: Session = Depends(get_db)):
    sql = """
    UPDATE player
    SET money = :money
    """
    await db.execute(text(sql), {"id": player.id, "money": player.money})
    await db.commit()

    sql_select = """
    SELECT * FROM player WHERE id = :id
    """
    result = await db.execute(text(sql_select), {"id": player.id})
    updated_player = result.fetchone()

    return dict(updated_player._mapping) if updated_player else None