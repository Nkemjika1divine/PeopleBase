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

if __name__ == '__main__':
    PeopleBase().cmdloop()