from faker import Faker
from random import randint, choice
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Customer, Player, Chat, Magic

from dotenv import load_dotenv
import os

load_dotenv()

MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")

DB_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:3306/{MYSQL_DATABASE}?charset=utf8"


engine = create_engine(DB_URL)

Session = sessionmaker(bind=engine)
session = Session()

faker = Faker()


def create_magic():
    new_magic = Magic(id=0, magic_name="テスト", effect="6面揃う")
    session.add(new_magic)
    session.commit()


def main():
    create_magic()


if __name__ == "__main__":
    main()
