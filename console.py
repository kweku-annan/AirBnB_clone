#!/usr/bin/python3
"""Contains the entry point of the command interpreter:"""
import cmd


class HBNBCommand(cmd.Cmd):
    """A class that defines the entry point of the AirBnB Clone Project"""
    prompt = "(hbnb) "

    def do_quit(self, s):
        """Quit command to exit the program\n"""
        return (True)

    def do_EOF(self, s):
        """EOF to exit the interpreter"""
        return (True)

    def emptyline(self):
        """Does nothing when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
