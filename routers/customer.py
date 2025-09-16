import random
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from db import get_db
from models.customer import Customer

router = APIRouter()


@router.get("/customer")
async def get_customer(db: Session = Depends(get_db)):
    results = await db.execute(select(Customer))
    customers = results.scalars().all()
    return random.choice(customers)
