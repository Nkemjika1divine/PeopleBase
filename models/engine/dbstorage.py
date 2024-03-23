#!/usr/bin/python3
import os
from datetime import date
from dotenv import load_dotenv
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
                    class_name = obj.__class__.__name__
                    key = class_name + "." + obj.id
                    result[key] = obj
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
        """Gets the runnung seession"""
        return self.__session
    

    def count(self, cls=None):
        from models import storage
        """count the number of objects in storage"""
        if not cls:
            count = 0
            all_classes = storage.all()
            for i in all_classes:
                count += 1
            return count
        else:
            count = len(storage.all(cls))

        return count
    

    def get_dataset(self, phone_or_email):
        """Gets an object in the dataset table"""
        from models import storage
        all_cls = storage.all("Dataset")
        for key, value in all_cls.items():
            data_id = key.split(".")[1]
            if get_column_value(session=self.__session, table_name=Dataset, row_id=data_id, column_name="email") == phone_or_email:
                return value
            if get_column_value(session=self.__session, table_name=Dataset, row_id=data_id, column_name="phone_number") == phone_or_email:
                return value
    

    def get_user(self, username):
        """gets an object in the user table"""
        from models import storage
        all_cls = storage.all("User")
        for key, value in all_cls.items():
            data_id = key.split(".")[1]
            if get_column_value(session=self.__session, table_name=User, row_id=data_id, column_name="username") == username:
                return value
    

    def get_crime(self, phone_or_email, crime_id):
        """Gets all the crimes of a dataset object"""
        from models import storage
        crimes = storage.get_dataset_crime(phone_or_email)
        for key, value in crimes.items():
            crime_value = value.to_dict()
            if crime_value["id"] == crime_id:
                return value


    def get_dataset_crime(self, phone_or_email):
        """Retrieves the crimes of a user"""
        from models import storage
        all_cls = storage.all("Dataset")
        crimes = {}
        for key, value in all_cls.items():
            data_id = key.split(".")[1]
            if get_column_value(session=self.__session, table_name=Dataset, row_id=data_id, column_name="email") == phone_or_email or get_column_value(session=self.__session, table_name=Dataset, row_id=data_id, column_name="phone_number") == phone_or_email:
                all_crimes = storage.all("Crime")
                for crime_key, crime_value in all_crimes.items():
                    crime_id = crime_key.split(".")[1]
                    if get_column_value(session=self.__session, table_name=Crime, row_id=crime_id, column_name="criminal_id") == data_id:
                        crimes[crime_key] = crime_value
                return crimes
    

    def get_activity(username, activity_id):
        """Retreives an activity"""
        from models import storage
        all_activity = storage.get_user_activity(username)
        for key, value in all_activity.items():
            activity_key = key.split(".")[1]
            if activity_key == activity_id:
                return value


    def get_user_activity(self, username):
        """Retrieves the crimes of a user"""
        from models import storage
        all_cls = storage.all("User")
        activities = {}
        for key, value in all_cls.items():
            data_id = key.split(".")[1]
            if get_column_value(session=self.__session, table_name=User, row_id=data_id, column_name="username") == username:
                all_activities = storage.all("Activity")
                for activity_key, activity_value in all_activities.items():
                    activity_id = activity_key.split(".")[1]
                    if get_column_value(session=self.__session, table_name=Activity, row_id=activity_id, column_name="user_id") == data_id:
                        activities[activity_key] = activity_value
                return activities
    

    def check_dataset_duplicity(self, obj):
        """checks if there's a duplicate value for phone number or email
        Returns 1 for email and 2 for username and 3 for phone number"""
        from models import storage
        all_dataset = storage.all("Dataset")
        for key in all_dataset.keys():
            dataset_id = key.split(".")[1]
            if get_column_value(session=self.__session, table_name=Dataset, row_id=dataset_id, column_name="email") == obj:
                return 1
            elif get_column_value(session=self.__session, table_name=Dataset, row_id=dataset_id, column_name="phone_number") == obj:
                return 2
        return None
    

    def check_user_duplicity(self, obj):
        """checks if there's a duplicate value for username, phone number or email
        Returns 1 for email, 2 for username and 3 for phone number"""
        from models import storage
        all_users = storage.all("User")
        for key in all_users.keys():
            user_id = key.split(".")[1]
            if get_column_value(session=self.__session, table_name=User, row_id=user_id, column_name="email") == obj:
                return 1
            elif get_column_value(session=self.__session, table_name=User, row_id=user_id, column_name="username") == obj:
                return 2
            elif get_column_value(session=self.__session, table_name=User, row_id=user_id, column_name="phone_number") == obj:
                return 3
        return None
    

    def check_activity_foreign_key(self, obj):
        """checks if the user_id in the parsed data exists in the user table
        Returns True if it exists"""
        from models import storage
        all_users = storage.all("User")
        for key in all_users:
            user_id = key.split(".")[1]
            if user_id == obj:
                return True
        return False
    

    def check_crime_foreign_key(self, obj):
        """checks if the user_id in the parsed data exists in the user table
        Returns True if it exists"""
        from models import storage
        all_dataset = storage.all("Dataset")
        for key in all_dataset:
            dataset_id = key.split(".")[1]
            if dataset_id == obj:
                return True
        return False


def get_column_value(session=None, table_name=None, row_id=None, column_name=None):
    """Gets the value at a column of a table"""
    if table_name and row_id and column_name:
        row = session.query(table_name).get(row_id)
    if row:
        return getattr(row, column_name)
    else:
        return None


def print_requested_data(session=None, table_name=None, row_id=None, arg=None):
    """Prints a requested data to the console"""
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
    """prints a requested crime to the console"""
    if session and table_name and row_id and arg:
        print