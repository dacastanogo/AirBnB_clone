#!/usr/bin/python3
"""Modulee for the entry point of the command interpreter."""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models import storage, classes
from datetime import datetime
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class HBNBCommand(cmd.Cmd):

    """Command interpreter class"""

    prompt = "(hbnb)"
    allowed_classes = classes
    """
    _____________________$$$
    ____________________$___$
    _____________________$$$
    _____________________$_$
    _____________________$_$
    ___________________$$$_$$$
    _________________$$__$$$__$$$
    _______________$$__$$$$$$$___$
    ______________$_______________$
    _____________$_________________$
    _____________$_________________$
    _____________$_____$$$$$$$$$$$$$$$
    _____________$____$_______________$
    _____________$____$___$$$$$$$$$$$$$
    _____________$___$___$___________$$$
    _____________$___$___$_$$$___$$$__$$
    _____________$___$___$_$$$___$$$__$$
    _____________$___$___$___________$$$
    _____________$____$___$$$$$$$$$$$$$
    _____________$_____$$$$$$$$$$$$$$
    _____________$_________________$
    _____________$____$$$$$$$$$$$$$$
    _____________$___$__$__$__$__$
    _____________$__$$$$$$$$$$$$$$
    _____________$__$___$__$__$__$
    _____________$___$$$$$$$$$$$$$$$
    ____________$$$_________________$$$
    __________$$___$$$_________$$$$$___$$
    ________$$________$$$$$$$$$__________$$$
    _______$__$$_____________________$$$$___$$
    ____$$$$$___$$$$$$$$______$$$$$$$_______$_$
    __$______$$_________$$$$$$______________$_$$
    _$____$____$____________________________$_$_$
    _$_____$___$______________$$$$$$$$$$$___$_$_$$
    _$$$____$___$__$$$$$$$$$$$$__________$___$_$_$$
    $___$$$$____$__$_____________________$___$_$$_$
    $$$____$___$$__$_____________________$$__$_$__$
    $___$__$__$$___$______________________$__$$$__$
    $_____$$_$$____$_______________$$$____$__$_$__$
    """

    def do_create(self, command):
        """
        Creates a new instance of BaseModel.
        """
        if command == "" or command is None:
            print("** class name missing **")
            return

        tokens = command.split(" ")
        if tokens[0] not in self.allowed_classes():
            print("** class doesn't exist **")
        else:
            new = self.allowed_classes()[tokens[0]]()
            new.save()
            print(new.id)

    def do_show(self, command):
        """
        Prints the string representation of an instance.
        """
        tokens = command.split()
        objects = storage.all()
        try:
            if len(tokens) == 0:
                print("** class name missing **")
                return
            if tokens[0] in self.allowed_classes():
                if len(tokens) > 1:
                    key = tokens[0] + "." + tokens[1]
                    if key in objects:
                        show_obj = objects[key]
                        print(show_obj)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        except AttributeError:
            print("** instance id missing **")

    def do_destroy(self, command):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        if not command:
            print("** class name missing **")
            return
        tokens = command.split(" ")
        objects = storage.all()

        if tokens[0] in self.allowed_classes:
            if len(tokens) < 2:
                print("** instance id missing **")
                return
            name = tokens[0] + "." + tokens[1]
            if name not in objects:
                print("** no instance found **")
            else:
                obj_de = objects[name]
                """
                obj_de stands for object to destroy
                """
                if obj_de:
                    objs = storage.all()
                    del objs["{}.{}".format(type(obj_de).__name__, obj_de.id)]
                    storage.save()
        else:
            print("** class doesn't exist **")

    def do_all(self, command):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        objects = storage.all()
        instances = []
        if not command:
            for name in objects:
                instances.append(objects[name])
            print(instances)
            return
        tokens = command.split(" ")
        if tokens[0] in self.allowed_classes:
            for name in objects:
                if name[0:len(tokens[0])] == tokens[0]:
                    instances.append(objects[name])
            print(instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, command):
        """
        Update an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        """
        if not command:
            print("** class name missing **")
            return
        tokens = command.split(" ")
        objects = storage.all()
        if tokens[0] in self.allowed_classes:
            if len(tokens) < 2:
                print("** instance id missing **")
                return
            name = tokens[0] + "." + tokens[1]
            if name not in objects:
                print("** no instance found **")
            else:
                obj_update = objects[name]
                denied_access = ["id", "created_at", "updated_at"]
                if obj_update:
                    arguments = command.split(" ")
                    if len(arguments) < 3:
                        print("** attribute name missing **")
                    elif len(arguments) < 4:
                        print("** value missing **")
                    elif arguments[2] not in denied_access:
                        obj_update.__dict__[arguments[2]] = arguments[3]
                        obj_update.updated_at = datetime.now()
                        storage.save()
        else:
            print("** class doesn't exist **")

    def do_EOF(self, command):
        """
        End of file character handler.
        """
        print()
        return True

    def do_quit(self, command):
        """
        Exit the console.
        """
        return True

    def emptyline(self):
        """
        Don't do anything when you press ENTER.
        """
        pass

    def do_help(self, command):
        """
        Command lists all help details for each command
        """
        cmd.Cmd.do_help(self, command)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
