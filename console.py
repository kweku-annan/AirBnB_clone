#!/usr/bin/python3
"""Contains the entry point of the command interpreter:"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """A class that defines the entry point of the AirBnB Clone Project"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.

        If the class name is missing, print **class name missing **.
        If the class name doesn't exist, print **class doesn't exist**
        """
        if arg == "BaseModel" and len(arg.split()) == 1:
            base_model = BaseModel()
            base_model.save()
            print(base_model.id)
        elif len(arg.split()) < 1:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
        
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
