#!/usr/bin/python3
"""
Test Cases for City model
"""
import os
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class City_Testing(unittest.TestCase):
    """City Testing"""
    
    def Check_BaseModel_Inheritance(self):
        """
        Checks that City inherits from BaseModel
        """
        c1 = Ctate()
        self.assertEqual(issubclass(type(c1), BaseModel), True)

    def CheckName(self):
        """
        Checks for name and class attribute
        """
        self.assertEqual('name' in City.__dict__, True)

    def Check_created_at(self):
        """
        Checks for created_at from BaseModel
        """
        c1 = City()
        self.assertEqual(type(c1.created_at) is datetime, True)

    def Check_updated_at(self):
        """
        Checks for updated_at from BaseModel
        """
        c1 = City()
        self.assertEqual(type(c1.updated_at) is datetime, True)

    def CheckId(self):
        """
        Checks for a valid ID 
        """
        c1 = City()
        self.assertEqual(type(c1.id) is str, True)