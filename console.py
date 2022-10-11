#!/usr/bin/python3


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

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