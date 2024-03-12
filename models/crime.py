#!/usr/bin/python3
import os
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import Column, String, ForeignKey
from models.basemodel import BaseModel, Base
from models.dataset import Dataset

load_dotenv()

class Crime(BaseModel, Base):
    if os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "file":
        criminal_id = ""
        crime_committed = ""
        punishment = ""
    elif os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "db":
        __tablename__ = "crimes"
        criminal_id = Column(String(50), ForeignKey("dataset.id"), nullable=False)
        crime_committed = Column(String(200), nullable=False)
        punishment = Column(String(200), nullable=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)