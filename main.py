import uvicorn
from fastapi import FastAPI
from routers import customer, player

app = FastAPI()
app.include_router(customer.router)
app.include_router(player.router)


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0")
