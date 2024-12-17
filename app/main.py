from fastapi import FastAPI, HTTPException
from .models import loginRequest

app = FastAPI()

@app.post("/token")
async def login(data: loginRequest):
    return await get