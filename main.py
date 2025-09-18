import uvicorn
from fastapi import FastAPI
from routers import customer, player, magic

from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager
from google import genai
import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.genai_client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customer.router)
app.include_router(player.router)
app.include_router(magic.router)


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=port)
