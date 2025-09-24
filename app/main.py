from fastapi import FastAPI

app = FastAPI(root_path="/real-estate")

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}
