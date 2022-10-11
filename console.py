#!/usr/bin/python3
"""Is the console of project"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Define a console Class"""

    prompt = "(hbnb) "

    def do_quit(self, args):
        exit()

    def do_EOF(self, args):
        print("")
        exit()

    def do_empty_line(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()