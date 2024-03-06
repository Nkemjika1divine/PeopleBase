#!/usr/bin/python3
import os
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, Date, ForeignKey
from models.basemodel import BaseModel, Base
from models.user import User

load_dotenv()

class Activity(BaseModel, Base):
    if os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "file":
        user_id = ""
        information_accessed = ""
        date = ""
    elif os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "db":
        __tablename__ = "activities"
        user_id = Column(String(50), ForeignKey("users.id"), nullable=False)
        information_accessed = Column(String(500), nullable=False)
        date = Column(Date, default=datetime.utcnow, nullable=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)