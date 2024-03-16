#!/usr/bin/python3
import os
from dotenv import load_dotenv
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from models.basemodel import BaseModel, Base
from models.dataset import Dataset

load_dotenv()

class Crime(BaseModel, Base):
    if os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "file":
        criminal_id = ""
        crime_committed = ""
        punishment = ""
        duration_in_months = 0
        duration_starts = ""
        duration_ends = ""
    elif os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "db":
        __tablename__ = "crimes"
        criminal_id = Column(String(50), ForeignKey("dataset.id"), nullable=False)
        crime_committed = Column(String(200), nullable=False)
        punishment = Column(String(200), nullable=False)
        duration_in_months = Column(Integer, nullable=False)
        duration_starts = Column(Date, nullable=False)
        duration_ends = Column(Date, nullable=True)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)