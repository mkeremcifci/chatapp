from fastapi import HTTPException
from passlib.context import CryptContext
from app.security import verifyPassword, createAccessToken
from app.models import loginRequest, verifyRequest
from app.security import decodeAccessToken
from app.database.crud import DatabaseManager
from app.database.database import SessionLocal



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def getToken(data: loginRequest):
    username = data.username
    password = data.password
    db = SessionLocal()
    try:
        hashedPassword = DatabaseManager.getHashedPasswordByUsername(db,username)

        if hashedPassword is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        else:
            if not verifyPassword(password, hashedPassword):
                raise HTTPException(status_code=401, detail="Invalid credentials")
            id = DatabaseManager.getIdByUsername(db, username)
            accessToken = createAccessToken(id=id)
            return {"access_token": accessToken, "token_type":"bearer"}
    finally:
        db.close()
        
        
        
async def decodeToken(data:verifyRequest):
    payload = decodeAccessToken(token=data.token)
    userId = payload.get("sub")
    if userId is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"user_id": userId}

