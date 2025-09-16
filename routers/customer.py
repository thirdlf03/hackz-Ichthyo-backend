import random
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models.customer import Customer

router = APIRouter()

@router.get("/customer")
def get_customer(db: Session = Depends(get_db)):
    customers = db.query(Customer).all()
    return random.choice(customers)
