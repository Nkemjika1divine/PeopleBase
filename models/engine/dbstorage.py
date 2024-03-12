#!/usr/bin/python3
import os
from dotenv import load_dotenv
from models.basemodel import Base
from models.dataset import Dataset
from models.activity import Activity
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

load_dotenv()

classes = {"Dataset": Dataset,
           "User": User,
           "Activity": Activity
           }

class DBStorage:
    __session = None
    __engine = None

    def __init__(self):
        PEOPLEBASE_ENV = os.environ.get('PEOPLEBASE_ENV')
        PEOPLEBASE_DATABASE_NAME_TEST = os.environ.get('PEOPLEBASE_DATABASE_NAME_TEST')
        PEOPLEBASE_DATABASE_USER = os.environ.get('PEOPLEBASE_DATABASE_USER')
        PEOPLEBASE_DATABASE_PWD = os.environ.get('PEOPLEBASE_DATABASE_PWD')
        PEOPLEBASE_DATABASE_HOST = os.environ.get('PEOPLEBASE_DATABASE_HOST')
        PEOPLEBASE_DATABASE_PORT = os.environ.get('PEOPLEBASE_DATABASE_PORT')
        self.__engine = create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(PEOPLEBASE_DATABASE_USER,
                                                                                     PEOPLEBASE_DATABASE_PWD,
                                                                                     PEOPLEBASE_DATABASE_HOST,
                                                                                     PEOPLEBASE_DATABASE_PORT,
                                                                                     PEOPLEBASE_DATABASE_NAME_TEST),
                                                                                     pool_pre_ping=True)
        if PEOPLEBASE_ENV == "test":
            try:
                Base.metadata.drop_all(self.__engine)
            except Exception:
                print("No Table found in the database")
    
    def all(self, cls=None):
        """query on the current database session"""
        result = {}
        if cls is not None:
            for obj in self.__session.query(cls).all():
                ClassName = obj.__class__.__name__
                keyName = ClassName + "." + obj.id
                result[keyName] = obj
        else:
            for clss in classes:
                for obj in self.__session.query(clss).all():
                    ClassName = obj.__class__.__name__
                    keyName = ClassName + "." + obj.id
                    result[keyName] = obj
        return result

        """new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    new_dict[key] = obj
        return (new_dict)"""
    
    def new(self, obj):
        """add an object to the database"""
        self.__session.add(obj)
    
    def save(self):
        """commit all changes of the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the database"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """reloads from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()