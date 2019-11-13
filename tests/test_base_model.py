#!/usr/bin/python3
"""Test cases for BaseModel"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class Base_Model_Testing(unittest.TestCase):
    """BaseModel Testing"""
    def NewInstance(self):
        """
        Creating a new instance before each test
        """
        self.bm1 = BaseModel()

    def ClearTest(self):
        """
        Clearing previous instance before next test
        """
        del self.bm1

    def CheckId(self):
        """
        Looks for ID attribute in BaseModel
        """
        self.assertEqual(bm1.id is None, False)

    def CheckUUID(self):
        """
        Looks for Unique ID 
        """
        bm2 = BaseModel()
        self.assertNotEqual(self.bm1.id, bm2.id)

    def Check_ID_type(self):
        """
        Checks id is of str type
        """
        bm1 = BaseModel()
        self.assertEqual(type(self.bm1.id), str)

    def Check_CreatedAt(self):
        """
        Checks if created_at is datetime type
        """
        self.assertEqual(type(self.bm1.created_at), datetime)
    
    def Check_Created_at_Not_None(self):
        """
        Checks that created_at attribute isnt None
        """
        bm1 = BaseModel()
        self.assertEqual(bm1.created_at is None, False)


    def Check_UpdatedAt(self):
        """
        Checks if updated_at is datetime type
        """
        self.assertEqual(type(self.bm1.updated_at), datetime)
    
    def Check_Updated_at_Not_None(self):.
    
        """
        Checks that updated_at attribute isnt None
        """
        bm1 = BaseModel()
        self.assertEqual(bm1.updated_at is None, False)

    def Check_Save__Funct(self):
        """
        Checks if save method updates updated_at
        """
        previous_updated_at = self.bm1.updated_at
        self.bm1.save()
        self.assertNotEqual(previous_updated_at, self.bm1.updated_at)

    def Check_NewerDate_Updated(self):
        """
        Checks if new updated dater is newer than previous pre save() date
        """
        bm1 = BaseModel()
        upd1 = bm1.updated_at
        bm1.save()
        upd2 = bm1.updated_at
        self.assertEqual(upd1 < upd2, True)

    def Check_ReturnType(self):
        """
        Checks the return type to be __str__
        """
        self.assertEqual(str(self.bm1), "[BaseModel] ({}) {}".format(self.bm1.id, self.bm1.__dict__))

    def Check_to_dict(self):
        """
        Checks that to_dict method returns a dictionary
        """
        bm1 = BaseModel()
        dictionary1 = bm1.to_dict()
        self.assertEqual(type(dictionary1), dict)

    def Compare_Kwargs(self):
        """
        Compares kwargs and BaseModel Instances 
        """
        json = self.bm1.to_dict()
        bm2 = BaseModel(**json)
        self.assertEqual(self.bm1.id, bm2.id)
        self.assertEqual(self.bm1.created_at, bm2.created_at)
        self.assertEqual(self.bm1.updated_at, bm2.updated_at)
        self.assertNotEqual(self.bm1, bm2)