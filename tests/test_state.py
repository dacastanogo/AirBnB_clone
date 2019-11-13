#!/usr/bin/python3
"""
Test Cases for State model
"""

import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class State_Testing(unittest.TestCase):
    """State Testing"""
    
    def Check_BaseModel_Inheritance(self):
        """
        Checks that State inherits from BaseModel
        """
        st1 = State()
        self.assertEqual(issubclass(type(st1), BaseModel), True)

    def CheckName(self):
        """
        Checks for name and class attribute
        """
        self.assertEqual('name' in State.__dict__, True)

    def Check_created_at(self):
        """
        Checks for created_at from BaseModel
        """
        st1 = State()
        self.assertEqual(type(st1.created_at) is datetime, True)

    def Check_updated_at(self):
        """
        Checks for updated_at from BaseModel
        """
        st1 = State()
        self.assertEqual(type(st1.updated_at) is datetime, True)

    def CheckId(self):
        """
        Checks for a valid ID 
        """
        st1 = State()
        self.assertEqual(type(st1.id) is str, True)