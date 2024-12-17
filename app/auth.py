from fastapi import HTTPException
from passlib.context import CryptContext
from .security import verifyPassword, createAccessToken
from .models import loginRequest

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def getToken(data: loginRequest):
    username = data.username
    password = data.password
    
    fakeHashedPassword = pwd_context.hash("password")
    if not verifyPassword(password, fakeHashedPassword):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    accessToken = createAccessToken(username)
    return {"access_token": accessToken, "token_type":"bearer"}
