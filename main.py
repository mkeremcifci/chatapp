from app.database.crud import DatabaseManager
from app.database.database import SessionLocal




db = SessionLocal()
try:
    username = "Kerem"
    password = "password"
    bio = "Just a user 2"

    DatabaseManager.addNewUser(db, username=username, password = password, bio=bio)

finally:
    db.close()