import random
from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, text
from db import get_db
from pydantic import BaseModel
from models.customer import Customer
from typing import Optional
from schemas.message import MessageSchema
from google.genai import types

router = APIRouter()

class ActionRequest(BaseModel):
    action: str

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

@router.post("/customers/{customer_id}/action")
async def set_customer_action(customer_id: int, request: ActionRequest, db: Session = Depends(get_db),
):
    action_sql = """
        UPDATE customer SET status = :action_param WHERE id = :customer_id_param;
    """

    action_result = await db.execute(text(action_sql),
        {
            "action_param": request.action,
            "customer_id_param": customer_id,
        },
    )
    await db.commit()

    return {"message": "Action updated"}

@router.post("/customers/messages")
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

            YOU MUST: 客の情報を与えるので、必ずその情報に沿って筐体上に沿って返答してください。

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