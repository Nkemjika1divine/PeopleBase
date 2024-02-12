#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'time_created' or key == 'time_updated':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid4())
            self.time_created = datetime.now()
            self.time_updated = datetime.now()
            storage.new(self)
    
    def __str__(self):
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
    
    def to_dict(self):
        copy = self.__dict__.copy()
        copy['__class__'] = self.__class__.__name__
        copy['time_created'] = self.time_created.isoformat()
        copy['time_updated'] = self.time_updated.isoformat()
        return copy

    def save(self):
        self.time_updated = datetime.now()
        storage.new(self)
