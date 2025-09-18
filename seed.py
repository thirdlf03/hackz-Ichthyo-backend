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
    magic_data = [
        {
            "id": 1,
            "magic_name": "マフリアート",
            "effect": "耳元で謎の赤い生き物の歌が聞こえ続けるようになった。",
        },
        {
            "id": 2,
            "magic_name": "インセンディオ",
            "effect": "着てる服の後ろ半分だけ丸焦げになり、びん⚪︎っちゃまスタイルになった。",
        },
        {
            "id": 3,
            "magic_name": "オブリビエイト",
            "effect": "今まで使った金額を忘れ、貯金残高0円になるまで浪費を続けた。",
        },
        {
            "id": 4,
            "magic_name": "ウィンガーディアム・レビオーサ",
            "effect": "強制的に店外に飛ばされ、店を二度と見つけられなくなった。",
        },
        {"id": 5, "magic_name": "アグアメンティ", "effect": "ずぶ濡れになった。"},
        {
            "id": 6,
            "magic_name": "ルーモス",
            "effect": "スマホの懐中電灯が点いて消えなくなった。地味に嫌。",
        },
        {
            "id": 7,
            "magic_name": "イモビラス",
            "effect": "店内中のメダルが全身に張りつき、身動きが取れなくなった。",
        },
        {"id": 8, "magic_name": "くらえ", "effect": "蹴りました。"},
        {"id": 9, "magic_name": "おりゃ", "effect": "殴りました。"},
        {"id": 10, "magic_name": "ビビデバビデブー", "effect": "消し去りました。"},
        {
            "id": 11,
            "magic_name": "ちちんぷいぷい",
            "effect": "あまりの可愛さに客の機嫌が良くなった。",
        },
        {"id": 12, "magic_name": "バルス!", "effect": "店舗爆発！！！！！"},
    ]

    for magic in magic_data:
        new_magic = Magic(**magic)
        session.add(new_magic)

    session.commit()
    print(f"Added {len(magic_data)} magic records to database")


def main():
    create_magic()


if __name__ == "__main__":
    main()
