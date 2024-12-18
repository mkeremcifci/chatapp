from sqlalchemy.orm import Session
from app.database.models import User
from sqlalchemy.exc import IntegrityError
from app.security import hashPassword


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

    def getHashedPasswordByUsername(db : Session, username:str):
        user = db.query(User).filter(User.username == username).first()
        if user:
            return user.password
        return None

    def addNewUser(db:Session, username:str, password:str, bio : str = None, isOnline : bool = False):
        try:
            hashedPassword = hashPassword(password)
            newUser = User(username = username, password = hashedPassword, bio = bio, isOnline = isOnline)
            db.add(newUser)
            db.commit()
            db.refresh(newUser)
        except IntegrityError:
            raise ValueError("Bu kullanıcı adı zaten mevcut")


