#!/usr/bin/python3
"""
Test Cases for User model
"""
import os
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class User_Testing(unittest.TestCase):
    """User Testing"""
    
    def Check_BaseModel_Inheritance(self):
        """
        Checks that User inherits from BaseModel
        """
        am1 = Amenity()
        self.assertEqual(issubclass(type(am1), BaseModel), True)

    def CheckName(self):
        """
        Checks for name and class attribute
        """
        self.assertEqual('name' in Amenity.__dict__, True)

    def Check_created_at(self):
        """
        Checks for created_at from BaseModel
        """
        am1 = Amenity()
        self.assertEqual(type(am1.created_at) is datetime, True)

    def Check_updated_at(self):
        """
        Checks for updated_at from BaseModel
        """
        am1 = Amenity()
        self.assertEqual(type(am1.updated_at) is datetime, True)

    def CheckId(self):
        """
        Checks for a valid ID 
        """
        am1 = Amenity()
        self.assertEqual(type(am1.id) is str, True)
        