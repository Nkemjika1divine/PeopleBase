#!/usr/bin/python3
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, Date, Integer
from models.basemodel import BaseModel, Base

load_dotenv()

class Dataset(BaseModel, Base):
    if os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "file":
        first_name = ""
        middle_name = ""
        last_name = ""
        photo = ""
        photo_type = ""
        date_of_birth = ""
        gender = ""
        address = ""
        city = ""
        state = ""
        country = ""
        phone_number = ""
        email = ""
        nationality = ""
        occupation = ""
        education_level = ""
        marital_status = ""
    elif os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "db":
        __tablename__ = "dataset"
        first_name = Column(String(20), nullable=False)
        middle_name = Column(String(20), nullable=True)
        last_name = Column(String(20), nullable=False)
        photo = Column(String(300), nullable=False)
        photo_type = Column(String(30), nullable=False)
        date_of_birth = Column(Date, nullable=False)
        gender = Column(String(10), nullable=False)
        address = Column(String(150), nullable=False)
        city = Column(String(20), nullable=False)
        state = Column(String(20), nullable=False)
        country = Column(String(20), nullable=False)
        phone_number = Column(String(20), unique=True, nullable=False)
        email = Column(String(60), unique=True, nullable=False)
        nationality = Column(String(20), nullable=False)
        occupation = Column(String(20), nullable=False)
        education_level = Column(String(20), nullable=False)
        marital_status = Column(String(20), nullable=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)