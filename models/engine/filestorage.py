#!/usr/bin/python3
from models.basemodel import BaseModel

class FileStorage:
    __file_path = "filestorage.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        class_name = obj.__class__.__name__
        object_id = obj['id']
        obj_key = "{}.{}".format(class_name, object_id)
        self.all().update({obj_key: obj})
