#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.time_created = datetime.now()
        self.time_updated = datetime.now()
    
    def __str__(self):
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    """def all(self):"""
    
    def to_dict(self):
        copy = self.__dict__.copy()
        copy['__class__'] = self.__class__.__name__
        copy['time_created'] = self.time_created.isoformat()
        copy['time_updated'] = self.time_updated.isoformat()
        return copy

    def save(self):
        self.time_updated = datetime.now()
