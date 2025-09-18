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


def create_customers():
    customer_data = [
        {
            "id": 1,
            "name": "針井 歩田",
            "money": 2500,
            "profile": "景品が取れないとすぐ大声を出す。「店長を呼べ」が口癖",
            "level": 100,
            "status": "生存",
            "age": 22,
            "icon_url": "https://drive.google.com/file/d/1PR24ZeboTs9a9Y_WX2NsZEwHUsr_eTzo/view?usp=drive_link",
        },
        {
            "id": 2,
            "name": "葉甘 伊央似",
            "money": 500,
            "profile": "ギャルママ。100円玉を筐体の下に落としがち。子供を使って自分の主張をする。例：店員さんに取れやすくしてもらいな",
            "level": 20,
            "status": "生存",
            "age": 24,
            "icon_url": "https://drive.google.com/file/d/1FXjxQAndrFEQDTQFGM1wlvGOYOgxDuXk/view?usp=drive_link",
        },
        {
            "id": 3,
            "name": "丸 府甥",
            "money": 300,
            "profile": "クレーマーかつ店員へのだる絡みが多い。",
            "level": 45,
            "status": "生存",
            "age": 55,
            "icon_url": "https://drive.google.com/file/d/1qneAz29lCFioYGN7jZctZQL4cxFYjHsv/view?usp=sharing",
        },
        {
            "id": 4,
            "name": "土 美意",
            "money": 1,
            "profile": "転売ヤー。メルカリの相場を見ながらプレイしていてなんか嫌。",
            "level": 60,
            "status": "生存",
            "age": 82,
            "icon_url": "https://drive.google.com/file/d/1NrSy0Axscd5Lq80O0FIONGA3kzsPLZJA/view?usp=sharing",
        },
        {
            "id": 5,
            "name": "巣利座 凜",
            "money": 1000,
            "profile": "クレーン筐体のガラスに指紋をつけまくる。ゲームセンターを公園だと勘違いしている子供。",
            "level": 5,
            "status": "生存",
            "age": 8,
            "icon_url": "https://drive.google.com/file/d/14hjWe7YxLuGtLCYVcPifQYB5wFKRr7yM/view?usp=sharing",
        },
        {
            "id": 6,
            "name": "スネイプ",
            "money": 700,
            "profile": "「ニホンゴワカラナイ」という言葉ですべての盤面を切り抜けようとする。",
            "level": 10,
            "status": "生存",
            "age": 26,
            "icon_url": "https://drive.google.com/file/d/1w9vW0jJtFz7mqeCmN-V8cpj78nWjVQC3/view?usp=sharing",
        },
        {
            "id": 7,
            "name": "刃愚 李度",
            "money": 100,
            "profile": "メダルゲームをしながらスーパーのお惣菜を食べる。ご飯粒落としがちなおじいちゃん。",
            "level": 7,
            "status": "生存",
            "age": 70,
            "icon_url": "https://drive.google.com/file/d/1o9GZ2KKwADjG3wnYWi4DW2JVNtF0fNIi/view?usp=sharing",
        },
        {
            "id": 8,
            "name": "論 ウェイ図理胃",
            "money": 3000,
            "profile": "ウェイ系大学生。女性店員と連絡先を交換したがる。常にテンションが高く、店員とも友達のように話す",
            "level": 3,
            "status": "生存",
            "age": 20,
            "icon_url": "https://drive.google.com/file/d/1dI0cO3BxYj1jYpGAFgbCd6ZcIiFg2O-A/view?usp=sharing",
        },
        {
            "id": 9,
            "name": "段振 扉",
            "money": 5000,
            "profile": "100円入れるごとに「取れないです」と助けを求めてくる。「1000円も使ってるんだけど」と言いながら300円ほどしか使っていないこともしばしば",
            "level": 80,
            "status": "生存",
            "age": 32,
            "icon_url": "https://drive.google.com/file/d/1qVl-mbNTt42Gz4QH94VGpZmfBCI5OOGq/view?usp=sharing",
        },
        {
            "id": 10,
            "name": "例のあの人",
            "money": 10000,
            "profile": "良客。ゲームセンターには珍しい良客なため、店員も優しくなり過度なアシストをしてしまいがち。",
            "level": 0,
            "status": "生存",
            "age": 50,
            "icon_url": "https://drive.google.com/file/d/1moNDniKmMGJGo0JWx5q5rY9HVh2-HV_n/view?usp=sharing",
        },
    ]

    for customer in customer_data:
        new_customer = Customer(**customer)
        session.add(new_customer)

    session.commit()
    print(f"Added {len(customer_data)} customer records to database")


def clear_data():
    # Delete all existing data from tables
    session.query(Customer).delete()
    session.query(Magic).delete()
    session.commit()
    print("Cleared all existing data from database")


def main():
    clear_data()
    create_customers()
    create_magic()


if __name__ == "__main__":
    main()
