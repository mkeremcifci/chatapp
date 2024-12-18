from fastapi import FastAPI, HTTPException
from app.models import loginRequest, verifyRequest
from app.auth import getToken, decodeToken

app = FastAPI()

@app.post("/token")
async def login(data: loginRequest):
    return await getToken(data)

@app.post("/verify-token")
async def verifyToken(data : verifyRequest):
    return await decodeToken(data)
    