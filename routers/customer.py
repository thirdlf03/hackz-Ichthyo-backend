import random
from db import get_db
from fastapi import APIRouter
from models import customer
from  schemas import customer

router = APIRouter()

@router.get("/customer")
def get_customer(db: Session = Depends(get_db)):
	customers=db.query(customer).all()
    return random.choice(customers)
