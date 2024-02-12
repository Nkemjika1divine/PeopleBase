#!/usr/bin/python3
import json
import os
from models.basemodel import BaseModel
from models.person import Person

classes = {'BaseModel': BaseModel, 'Person': Person}

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

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict() #get the dictionary representation of the object
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)
    
    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                try:
                    objects = json.load(f)
                    for key, value in objects.items():
                        class_name = classes[objects[key]["__class__"]] #retreive the class name
                        class_object = class_name(**value) #assign the value of the object to the class name
                        self.__objects[key] = class_object #update the key
                except Exception as e:
                    pass