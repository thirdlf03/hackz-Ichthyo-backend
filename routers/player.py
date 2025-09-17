from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, text
from db import get_db
from models.player import Player
from schemas.player import PlayerSchema
from schemas.message import MessageSchema
from google.genai import types

router = APIRouter()


@router.get("/player")
async def get_player(db: Session = Depends(get_db)):
    sql = """
    SELECT * FROM player
    """

    result = await db.execute(text(sql))
    player = result.fetchone()

    return player._asdict()


@router.post("/player")
async def create_player(player: PlayerSchema, db: Session = Depends(get_db)):
    sql = """
    INSERT INTO player (id, money)
    VALUES (id, money)
    """

    await db.execute(text(sql), {"id": player.id, "money": player.money})
    await db.commit()

    sql_select = """
    SELECT * FROM player WHERE id = :id
    """
    result = await db.execute(
        text(sql_select), {"id": player.id, "money": player.money}
    )
    new_player = result.fetchone()

    return dict(new_player._mapping) if new_player else None


@router.put("/player/money")
async def update_money(player: PlayerSchema, db: Session = Depends(get_db)):
    sql = """
    UPDATE player
    SET money = :money
    """
    await db.execute(text(sql), {"id": player.id, "money": player.money})
    await db.commit()

    sql_select = """
    SELECT * FROM player WHERE id = :id
    """
    result = await db.execute(text(sql_select), {"id": player.id})
    updated_player = result.fetchone()

    return dict(updated_player._mapping) if updated_player else None

@router.post("/player/messages")
async def response_messages(message: MessageSchema, request: Request, db: Session = Depends(get_db)):
    get_customer_sql = """
    SELECT * FROM customer WHERE id = :customer_id
    """
    get_customer_result = await db.execute(text(get_customer_sql), {"customer_id": message.customer_id})
    customer = get_customer_result.fetchone()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    customer_data = dict(customer._mapping)

    client = request.app.state.genai_client 

    model = "gemini-2.5-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"{message.message}"),
            ],
        ),
        
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ), 
        system_instruction=[
            types.Part.from_text(text=f"""
            今からあなたにはゲームセンターの客として振る舞ってもらいます。

            YOU MUST: 客の情報を与えるので、必ずその情報に沿ってユーザーのメッセージに対して返答してください。
            名前は、{customer_data['name']}
            年齢は、{customer_data['age']} です。
            プロフィールは、{customer_data['profile']}
            レベルは、 {customer_data['level']} です。
            レベルというのは、客がどれだけ良くない客なのかを表すレベルで、レベルが高いほど良くない客です。
            レベルが高いほど怒りやすい客です。
        """),
        ],
    )
    response = ""
    
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response += chunk.text

    return response