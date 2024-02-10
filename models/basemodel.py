#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = uuid4()
        self.time_created = datetime.now()
        self.time_updated = datetime.now()

    def all(self):
    
    def to_dict(self):

    def save(self):
        
