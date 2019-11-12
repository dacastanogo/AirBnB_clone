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
    def new(self, obj)