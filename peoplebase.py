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

    def emptyline(self):
        return False

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

    def do_find(self, arg=None):
        """finds a data from the database"""
        print("Searchin...")
        if arg:
            print("trying to load storage")
            all_data = storage.all()
            if all_data:
                for data in all_data:
                    print(data)
            else:
                print("Nothing found")
    
    def do_create(self, arg=None):
        if arg and arg.lower() == "data":
            first_name = input("Enter first name: ")
            middle_name = input("Enter middle name: ")
            last_name = input("Enter last name: ")

            print("Name is {} {} {}".format(first_name, middle_name, last_name))

        

if __name__ == '__main__':
    PeopleBase().cmdloop()