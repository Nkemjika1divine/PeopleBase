#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from

Base = declarative_base()

class BaseModel:
    def __init__(self, *args, **kwargs):
        from models import storage
        if kwargs:
            import models.__init__
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
            storage.new(self)
    
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def to_dict(self):
        copy = self.__dict__.copy()
        copy['__class__'] = self.__class__.__name__
        if 'time_created' in copy:
            copy['time_created'] = self.time_created.isoformat()
        if 'time_updated' in copy:
            copy['time_updated'] = self.time_updated.isoformat()
        return copy

    def save(self):
        from models import storage
        self.time_updated = datetime.now()
        storage.new(self)
        storage.save()