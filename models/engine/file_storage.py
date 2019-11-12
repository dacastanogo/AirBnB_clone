#!/usr/bin/python3
"""Importing models using the FileStorage class """

import json


class FileStorage:
    """Class that serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        objkey = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[objkey] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        save_file = self.__file_path
        """k for key"""
        for key, i in self.__objects.items():
            new_dict[k] = item.to_dict()
        with open(save_file, "w", encoding='utf-8') as new_file:
            json.dump(new_dict, new_file)

    def reload(self):
        """Deserializes the JSON file to __objects only if the JSON file exists"""
        