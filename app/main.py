from fastapi import FastAPI, HTTPException
from app.models import loginRequest
from app.auth import getToken

app = FastAPI()

@app.post("/token")
async def login(data: loginRequest):
    return await getToken(data)
