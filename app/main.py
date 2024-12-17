from fastapi import FastAPI, HTTPException
from .models import loginRequest
from .auth import getToken
from app.auth import getToken


app = FastAPI()

@app.post("/token")
async def login(data: loginRequest):
    return await getToken(data)

    

