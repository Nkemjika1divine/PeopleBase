#!/usr/bin/python3
from models.basemodel import BaseModel
from models.person import Person

if __name__ == "__main__":
    user = Person()
    user.__str__()
    print(user.time_updated)
    user.save()
    print(user.time_updated)
    print(user.to_dict())