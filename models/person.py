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
        id = Column(Integer, primary_key=True, nullable=False)
        first_name = Column(String(20), nullable=False)
        middle_name = Column(String(20))
        last_name = Column(String(20), nullable=False)
        photo = Column(String(300), nullable=False)
        photo_type = Column(String(30), nullable=False)
        date_of_birth = Column(Date, nullable=False)
        gender = Column(String(10), nullable=False)
        address = Column(String(150), nullable=False)
        city = Column(String(20), nullable=False)
        state = Column(String(20), nullable=False)
        country = Column(String(20), nullable=False)
        phone_number = Column(String(20), nullable=False)
        email = Column(String(60), nullable=False)
        nationality = Column(String(20), nullable=False)
        occupation = Column(String(20), nullable=False)
        education_level = Column(String(20), nullable=False)
        marital_status = Column(String(20), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialize person"""
        super().__init__(*args, **kwargs)

def search(line=None):
    from models.engine.dbstorage import DBStorage
    from models.__init__ import storage

    if line:
        similar_objects = {}
        all_objects = DBStorage.all()
        if os.path.isfile(line):
            for obj in all_objects:
                similarity = check_image(obj.photo, line)
                if similarity == True:
                    obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    similar_objects[obj_key] = obj
            return True
        else:
            for obj in all_objects:
                if obj.phone_number == line or obj.email == line:
                    obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    similar_objects[obj_key] = obj
            return True