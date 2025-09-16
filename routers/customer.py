import random
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, text
from db import get_db
from models.customer import Customer

router = APIRouter()


@router.get("/customer")
async def get_customer(db: Session = Depends(get_db)):
    sql = """
    SELECT * FROM customer ORDER BY RAND() LIMIT 1;
    """

    result = await db.execute(text(sql))
    customer = result.fetchone()

    if customer is None:
        return {"error": "No customer found"}
    
    return customer._asdict()
