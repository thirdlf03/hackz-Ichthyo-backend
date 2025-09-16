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


def create_customer(num=3):
    for x in range(num):
        new_customer = Customer(
            name=faker.first_name(),
            age=randint(1, 20),
            money=randint(100, 1000),
            profile=faker.sentence(),
            level=randint(1, 10),
            status=choice(["active", "inactive", "premium"]),
        )
        session.add(new_customer)
        session.commit()


def create_player(num=5):
    for x in range(num):
        new_player = Player(money=randint(100, 500))
        session.add(new_player)
        session.commit()


def main():
    print("シードデータを作成中...")
    create_customer(5)
    print("顧客データを作成しました")

    create_player(3)
    print("プレイヤーデータを作成しました")


if __name__ == "__main__":
    main()
