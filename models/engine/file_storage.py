#!/usr/bin/python3
"""
Importing models using the FileStorage class
"""

import json
import models
import os.path


class FileStorage:
    """
    Class that serializes instances to a JSON
    file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        objkey = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[objkey] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = dict()
        for key, value in self.__objects.items():
            obj_dict = value.to_dict()
            new_dict[key] = obj_dict
        new_json = json.dumps(new_dict)
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(new_json)

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
        """
        Deserializes the JSON file to __objects only if the JSON file exists
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                data = json.loads(f.read())
                new_dict = dict()
                for key, value in data.items():
                    classes = value['__class__']
                    self.__objects[key] = globals()[classes](**value)

        except Exception:
            pass