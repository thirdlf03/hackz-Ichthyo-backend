import random
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, text
from db import get_db
from models.customer import Customer
from typing import Optional

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

@router.get("/customers/{customer_id}/chat")
async def get_customer_chat(customer_id: int, db: Session = Depends(get_db)):
    chat_sql = """
        SELECT message FROM chat WHERE customer_id = :customer_id_param;
        """

    chat_result = await db.execute( text(chat_sql), {"customer_id_param": customer_id} )
    chat = chat_result.scalars().all()

    return chat

@router.get("/customers")
async def get_customer_status(status: Optional[str] = None, db: Session = Depends(get_db)):
    status_sql = """
    SELECT * FROM customer
    """
    params = {}

    if status:
        status_sql += " WHERE status = :status_param"
        params["status_param"] = status

    status_result = await db.execute(text(status_sql), params)

    customers = status_result.mappings().all()

    return customers
