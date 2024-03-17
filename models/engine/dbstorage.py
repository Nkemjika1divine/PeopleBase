#!/usr/bin/python3
import os
from datetime import date
from dotenv import load_dotenv
from models import storage
from models.basemodel import Base
from models.dataset import Dataset
from models.activity import Activity
from models.crime import Crime
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


load_dotenv()


classes = {"Dataset": Dataset,
           "User": User,
           "Activity": Activity,
           "Crime": Crime
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
            for obj in self.__session.query(classes[cls]).all():
                ClassName = obj.__class__.__name__
                keyName = ClassName + "." + obj.id
                result[keyName] = obj
        else:
            for cls in classes.values():
                for obj in self.__session.query(cls).all():
                    ClassName = obj.__class__.__name__
                    keyName = ClassName + "." + obj.id
                    result[keyName] = obj
        return result


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


    def get_session(self):
        return self.__session
    

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for a_class in all_class:
                count += len(storage.all(a_class).values())
        else:
            count = len(storage.all(cls).values())

        return count


def get_column_value(session=None, table_name=None, row_id=None, column_name=None):
        if table_name and row_id and column_name:
            row = session.query(table_name).get(row_id)
        if row:
            return getattr(row, column_name)
        else:
            return None


def print_requested_data(session=None, table_name=None, row_id=None, arg=None):
    if session and table_name and row_id and arg:
        print("Information associated with requested entry [{}]:".format(arg))
        print("Name: {} {} {}".format(get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="first_name"),
                                       get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="middle_name"),
                                       get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="last_name")))
        print("Date of Birth: {}".format(get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="date_of_birth")))
        print("Age: {} years".format((date.today() - get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="date_of_birth")) / 365.25))
        print("Gender: {}".format(get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="gender")))
        print("Nationality: {}".format(get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="nationality")))
        print("Residential Address: {}, {}, {}, {}.".format(get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="address"),
                                                            get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="city"),
                                                            get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="state"),
                                                            get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="country")))
        print("Phone Number: {}".format(get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="phone_number")))
        print("Email Address: {}".format(get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="email")))
        print("Phone Number: {}".format(get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="phone_number")))
        print("Marital Status: {}".format(get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="marital_status")))
        print("Occupation: {}".format(get_column_value(session=session, table_name=table_name, row_id=row_id, column_name="occupation")))

def print_requested_crime(session=None, table_name=None, row_id=None, arg=None):
    if session and table_name and row_id and arg:
        print