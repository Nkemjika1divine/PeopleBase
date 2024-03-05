#!/usr/bin/python3
from dotenv import load_dotenv
from uuid import uuid4
import os
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import declarative_base

load_dotenv()

Base = declarative_base()

class BaseModel:
    if os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "db":
        __abstract__ = True
        id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
        time_created = Column(DateTime, default=datetime.utcnow, nullable=False)
        time_updated = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        # from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'time_created' or key == 'time_updated':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.time_created = datetime.now()
            self.time_updated = datetime.now()
    
    def to_dict(self):
        copy = self.__dict__.copy()
        copy['__class__'] = self.__class__.__name__
        if 'time_created' in copy:
            copy['time_created'] = self.time_created.isoformat()
        if 'time_updated' in copy:
            copy['time_updated'] = self.time_updated.isoformat()
        if "_sa_instance_state" in copy:
            del copy["_sa_instance_state"]
        return copy

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        from models import storage
        self.time_updated = datetime.now()
        storage.new(self)
        storage.save()
    
    def delete(self):
        from models import storage
        """delete the current instance from the storage"""
        storage.delete(self)