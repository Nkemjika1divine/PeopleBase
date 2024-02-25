#!/usr/bin/python3
import os
from sqlalchemy import create_engine, Column, String, Date, Integer
from models.basemodel import BaseModel, Base
from dotenv import load_dotenv

load_dotenv()

class Person(BaseModel, Base):
    if os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "file":
        print("in file")
    elif os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "db":
        id = Column(Integer, primary_key=True)
        date_registered = Column(Date)
        date_updated = Column(Date)
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