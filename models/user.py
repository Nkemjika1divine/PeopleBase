#!/usr/bin/python3
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String
from models.basemodel import BaseModel, Base

load_dotenv()

class User(BaseModel, Base):
    if os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "file":
        email = ""
        address = ""
        phone_number = ""
        password = ""
        role = "user"
    elif os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "db":
        __tablename__ = "users"
        email = Column(String(60), nullable=False, unique=True)
        address = Column(String(500), nullable=False)
        phone_number = Column(String(20), nullable=False, unique=True)
        password = Column(String(20), nullable=False, unique=True)
        role = Column(String(10), default="user", nullable=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
