#!/usr/bin/python3
"""is the console of project"""


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()