#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
import models
from models.base_model import BaseModel
from models import storage
import json

class HBNBCommand(cmd.Cmd):

    """Command interpreter class"""

    prompt = "(hbnb)"
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

        tokens = command.split(" ")
        if tokens[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            new = storage.classes()[tokens[0]]()
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
            if tokens[0] in storage.classes:
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
            

    def do_EOF(self,command):
        """
        End of file character handler.
        """
        print()
        return True

    def do_quit(self,command):
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
