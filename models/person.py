#!/usr/bin/python3
import os
from sqlalchemy import create_engine, Column, String, Date, Integer
from models.basemodel import BaseModel
from dotenv import load_dotenv

load_dotenv()

class Person(BaseModel):
    if os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "file":
        print("in file")
    elif os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "db":
        pass
    """id = Column(Integer, primary_key=True)
    date_registered = Column(Date)
    date_updated = Column(Date)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    phone_number = Column(String)
    email = Column(String)
    nationality = Column(String)
    occupation = Column(String)
    education_level = Column(String)
    marital_status = Column(String)"""