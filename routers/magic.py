from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy import select, text
from db import get_db
from models.magic import Magic
from schemas.magic import MagicSchema

router = APIRouter()


@router.get("/magic")
async def get_magic(magic_name: str, db: Session = Depends(get_db)):
    chat_sql = """
    SELECT * FROM magic WHERE magic_name = :magic_name
    """
    result = await db.execute(text(chat_sql), {"magic_name": magic_name})
    magic = result.fetchone()

    if magic is None:
        raise HTTPException(status_code=404)
    else:
        return {"effect": magic.effect}
