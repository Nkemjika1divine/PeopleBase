#!/usr/bin/python3
import os
from sqlalchemy import create_engine, Column, String, Date, Integer
from models.basemodel import BaseModel, Base
from dotenv import load_dotenv

load_dotenv()

class Person(BaseModel, Base):
    if os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "file":
        id = ""
        first_name = ""
        middle_name = ""
        last_name = ""
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
        __tablename__ = "persons"
        id = Column(Integer, primary_key=True)
        first_name = Column(String(20))
        middle_name = Column(String(20))
        last_name = Column(String(20))
        date_of_birth = Column(Date)
        gender = Column(String(10))
        address = Column(String(150))
        city = Column(String(20))
        state = Column(String(20))
        country = Column(String(20))
        phone_number = Column(String(20))
        email = Column(String(60))
        nationality = Column(String(20))
        occupation = Column(String(20))
        education_level = Column(String(20))
        marital_status = Column(String(20))

    def __init__(self, *args, **kwargs):
        """initialize person"""
        super().__init__(*args, **kwargs)