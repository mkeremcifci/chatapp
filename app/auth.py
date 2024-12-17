from fastapi import HTTPException
from passlib.context import CryptContext
from .security import verifyPassword, createAccessToken
from .models import loginRequest
from app.database.crud import DatabaseManager
from app.database.database import SessionLocal



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def getToken(data: loginRequest):
    username = data.username
    password = data.password
    db = SessionLocal()
    try:
        id = DatabaseManager.getIdByUsername(db,username)
        
        fakeHashedPassword = pwd_context.hash("password")
        if id == None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        else:
            if not verifyPassword(password, fakeHashedPassword):
                raise HTTPException(status_code=401, detail="Invalid credentials")
            accessToken = createAccessToken(id=id)
            return {"access_token": accessToken, "token_type":"bearer"}
    finally:
        db.close()
