#!/usr/bin/python3
import cmd
from models.engine.dbstorage import DBStorage
from models import storage
from models.dataset import Dataset
from models.user import User
from models.activity import Activity

classes = {"Dataset": Dataset,
           "User": User,
           "Activity": Activity
           }

class PeopleBase(cmd.Cmd):
    prompt = "PeopleBase: "

    def do_quit(self, arg):
        return True
    
    def do_exit(self, arg):
        return True
    
    def do_EOF(self, arg):
        return True
    
    def help_exit(self):
        print("'exit' exits the program")
    
    def help_quit(self):
        print("'quit' exits the program")

    def do_find(self, arg):
        """finds a data from the database"""
        print("Searchin...")

        all_data = storage.all()
        if all_data:
            for data in all_data:
                print(data)
        else:
            print("Nothing found")

        

if __name__ == '__main__':
    PeopleBase().cmdloop()