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
        for k, item in self.__objects.items():
            new_dict[k] = item.to_dict()
        with open(save_file, "w", encoding='utf-8') as new_file:
            json.dump(new_dict, new_file)

    def classes(self):
        """
        Returns a dictionary of valid classes and their references.
        """
        
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes


    def reload(self):
        """Deserializes the JSON file to __objects only if the JSON file exists"""
    try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for k, v in (json.load(f)).items():
                    """k and v for key and value"""
                    v = eval(v["__class__"])(**v)
                    self.__objects[key] = v
        except FileNotFoundError:
            pass