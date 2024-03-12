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
        if arg:
            print("Looking for {}".format(arg))
            all_data = storage.all(arg)
            if all_data:
                print("{} found".format(arg))
                for key, value in all_data.items():
                    print("{}: {}".format(key, value))
            else:
                print("{} not found".format(arg))
        else:
            print("Looking for all data in the Database")
            all_data = storage.all()
            if all_data:
                print("Data found")
                for key, value in all_data.items():
                    print("{}: {}".format(key, value))
            else:
                print("There is no data in the Database")
    
    def do_create(self, arg=None):
        if arg and arg.lower() == "new data":
            print("*****Please endeavor to follow the instructions.*****\n**If you encounter an error, you will have to start afresh.**")
            first_name = input("Enter first name: ")
            middle_name = input("Enter middle name: ")
            last_name = input("Enter last name: ")
            photo = input("Enter path to photo: ")
            date_of_birth = input("Enter Date of Birth (Format = yyyy-mm-dd): ")
            gender_variable = input("Enter gender (M/F): ")
            if gender_variable.lower() == "male" or gender_variable.lower() == "m":
                gender = "Male"
            elif gender_variable.lower() == "female" or gender_variable.lower() == "f":
                gender = "Female"
            address = input("Enter Address: ")
            city = input("Enter City: ")
            state = input("Enter State: ")
            country = input("Enter Country of residence: ")
            nationality = input("Enter Country of Origin: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email Address: ")
            occupation = input("Enter Occupation: ")
            education_level = input("Enter Highest Educational Qualification (Ph.D/Masters/B.Sc./B.A/SSCE): ")
            marital_status = input("Enter Marital status (Single/Married/Engaged): ")

            try:
                data = Dataset(first_name=first_name,
                            middle_name=middle_name,
                            last_name=last_name,
                            photo=photo,
                            date_of_birth=date_of_birth,
                            gender=gender,
                            address=address,
                            city=city,
                            state=state,
                            country=country,
                            nationality=nationality,
                            phone_number=phone_number,
                            email=email,
                            occupation=occupation,
                            education_level=education_level,
                            marital_status=marital_status)
                storage.new(data)
                storage.save()
                print("{} {} {} has been added to the database".format(first_name, middle_name, last_name))
            except Exception as e:
                print("Error: ", e)

        

if __name__ == '__main__':
    PeopleBase().cmdloop()