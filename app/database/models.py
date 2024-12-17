from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    bio = Column(String, nullable=True)
    lastLogin = Column(DateTime, default=func.now())
    createdAt = Column(DateTime, default=func.now())
    isOnline = Column(Boolean, default=False)
    
