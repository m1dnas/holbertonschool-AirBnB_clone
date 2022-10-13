#!/usr/bin/python3
"""is the console of the project"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Define a console Class"""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """funtion quit"""
        exit()

    def do_EOF(self, l):
        """function EOF"""
        print("")
        exit()

    def emptyline(self):
        """Function emptyline"""
        pass

    def create(self, args):
        """Creates a new instance of BaseModel, saves it & prints the id"""
        if not arg:
            print("** class name missing **")
        # Evaluates the expression args to check if it exist
        try:
            instance = eval(args)()
            instance.save()
            print(instance.id)
        except:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
