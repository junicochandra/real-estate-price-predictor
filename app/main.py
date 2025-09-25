from fastapi import FastAPI, Depends
from app.adapters.routers import arithmetic
from pydantic import BaseModel, Field

app = FastAPI(root_path="/real-estate")
class User(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(gt=0, lt=120)

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@app.post("/hello")
def say_hello(user: User):
    return {"message": f"Halo {user.name}, I old {user.age} years. Welcome!"}

@app.get("/goodbye/{name}")
def say_goodbye(user: User = Depends()):
    return {"message": f"Goodbye {user.name}, I old {user.age} years. See you again!"}

app.include_router(arithmetic.router)