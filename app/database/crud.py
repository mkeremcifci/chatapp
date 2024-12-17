from app.database.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 
from app.database.models import User 


class DatabaseManager:
    def getPasswordByUsername(db: Session, username: str):
        user = db.query(User).filter(User.username == username).first()
        if user:
            return user.password
        return None
    
    def getIdByUsername(db : Session, username:str):
        user = db.query(User).filter(User.username == username).first()
        if user:
            return user.id
        return None