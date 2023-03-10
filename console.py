#!/usr/bin/python3
"""
Program that contains the entry point of the command interpreter
"""

import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place

class_list = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    intro = "\nThis is the best python command interpreter ever made.\n"
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Command that creates a new instance of the BaseModel class,
        saves it (to the JSON file) and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return

        elif arg not in class_list:
            print("** class doesn't exist **")
            return

# eval creates a class with the given argument arg

        inst = eval(arg)()
        inst.save()
        print(inst.id)

    def do_show(self, arg):
        """ 
        Prints the string representation of an instance based on the class name and id.
        """

        if arg == "":
            print("** class name missing **")
            return

        arg = arg.split()

        if arg[0] not in class_list:
            print("** class doesn't exist **")
            return

        elif len(arg) == 1:
            print("** instance id missing **")
            return

        dict = storage.all()
        for key, value in dict.items():
            if f"{arg[0]}.{arg[1]}" == key:
                print(dict[key])
                return

        print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """

        if arg == "":
            print("** class name missing **")
            return

        arg = arg.split()

        if arg[0] not in class_list:
            print("** class doesn't exist **")
            return

        elif len(arg) == 1:
            print("** instance id missing **")
            return

        dict = storage.all()
        for key, value in dict.items():
            if f"{arg[0]}.{arg[1]}" == key:
                del (dict[key])
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        arg = arg.split()
        str_list = []
        obj_dict = storage.all()

        if len(arg) == 0:
            for key, value in obj_dict.items():
                str_list.append(str(value))
            print(str_list)
            return

        elif len(arg) == 1:
            if arg[0] in class_list:
                for key, value in obj_dict.items():
                    if arg[0] in key:
                        str_list.append(str(value))
                print(str_list)
            else:
                print("** class doesn't exist **")
                return

    def do_update(self, arg):
        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
            return

        try:
            model = eval(arg[0])
        except Exception as e:
            print("** class doesn't exist **")
            return

        if len(arg) == 1:
            print("** instance id missing **")
            return

        dict = storage.all()
        not_found = 1
        for key, value in dict.items():
            if f"{arg[0]}.{arg[1]}" == key:
                not_found = 0
                continue
        if not_found == 1:
            print("** no instance found **")
            return

        if len(arg) == 2:
            print("** attribute name missing **")
            return

        if len(arg) == 3:
            print("** value missing **")
            return

        dict = storage.all()
        for key, value in dict.items():
            if f"{arg[0]}.{arg[1]}" == key:
                if type(arg[3]) is int:
                    setattr(value, arg[2], int(arg[3]))
                elif type(arg[3]) is float:
                    setattr(value, arg[2], float(arg[3]))
                else:
                    setattr(value, arg[2], arg[3].strip('"'))
        storage.save()

    def do_quit(self, arg):
        """
        Command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Command to exit the program by typing EOF or CTRL+D
        """
        return True

    def emptyline(self):
        """
        Empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
