#!/usr/bin/python3
"""Command Interpreter module"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Command Interpreter class for AirBnB project"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit command interpreter gracefully"""
        print()
        return True

    def do_quit(self, line):
        """Exit command interpreter"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ = "__main__":
    HBNBCommand().cmdloop()
