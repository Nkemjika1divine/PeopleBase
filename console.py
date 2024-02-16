#!/usr/bin/python3
import cmd

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

    def do_create(self, arg):
        """Creates an instance of a class"""
        first_name = str(input("First Name: "))
        middle_name = str(input("Middle Name: "))
        surname = str(input("Surname: "))
        print("My full name is {} {} {}".format(first_name, middle_name, surname))

        

if __name__ == '__main__':
    PeopleBase().cmdloop()