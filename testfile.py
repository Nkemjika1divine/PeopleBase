#!/usr/bin/python3
from models.basemodel import BaseModel
from models.engine.filestorage import FileStorage
from models.person import Person
from models import storage

if __name__ == "__main__":
    all_objs = storage.all()
    count = 0
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)
        count += 1
    
    print("-- Number of Objects --")
    print(count)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)