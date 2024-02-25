#!/usr/bin/python3
import os
from models.basemodel import Base
from models.person import Person
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {"Person": Person}

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        PEOPLEBASE_ENV = os.environ.get('PEOPLEBASE_ENV')
        PEOPLEBASE_DATABASE_NAME = os.environ.get('PEOPLEBASE_DATABASE_NAME')
        PEOPLEBASE_DATABASE_USER = os.environ.get('PEOPLEBASE_DATABASE_USER')
        PEOPLEBASE_DATABASE_PWD = os.environ.get('PEOPLEBASE_DATABASE_PWD')
        PEOPLEBASE_DATABASE_HOST = os.environ.get('PEOPLEBASE_DATABASE_HOST')
        PEOPLEBASE_DATABASE_PORT = os.environ.get('PEOPLEBASE_DATABASE_PORT')
        self.__engine = create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(PEOPLEBASE_DATABASE_USER, PEOPLEBASE_DATABASE_PWD, PEOPLEBASE_DATABASE_HOST, PEOPLEBASE_DATABASE_PORT, PEOPLEBASE_DATABASE_NAME), pool_pre_ping=True)
        if PEOPLEBASE_ENV == "test":
            try:
                Base.metadata.drop_all(self.__engine)
            except Exception:
                print("No Table found in the database")
    
    def all(self):
        """Returns all objects in the database"""
        all_objects = {}
        objects = self.__session.query().all()
        if objects:
            for obj in objects:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                all_objects[key] = obj
        return all_objects
    
    def new(self, obj):
        """adds a new object to the database"""
        self.__session.add(obj)
    
    def save(self):
        """Commits the changes made to the database"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Deletes an object from the database if not none and the object exists"""
        if obj:
            try:
                self.__session.delete(obj)
            except Exception:
                print("Data not found")
        
    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session