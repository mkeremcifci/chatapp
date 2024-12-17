from app.database.crud import DatabaseManager
from app.database.database import SessionLocal
from sqlalchemy.orm import Session


db = SessionLocal()
try:
    username = "john_doe"
    password = DatabaseManager.getPasswordByUsername(db, username)
    
    if password:
        print(f"Kullanıcı adı:{username} - parola {password}")
    else:
        print(f"{username} kullanıcısı bulunamadı")
finally:
    db.close()