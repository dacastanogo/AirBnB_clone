#!/usr/bin/python3
"""
Unittest for base_model
"""
import unittest
from models.base_model import BaseModel
import pep8
import datetime


class Test_BaseModel(unittest.TestCase):
    """
    Test class BaseModel
    """
    def test_pep8(self):
        """Pep8 Test"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """Checks if the docstring exists for each method and constructor"""
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_hasattribute(self):
        """Tests if the instance of BaseModel have been correctly made"""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "__init__"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "id"))

    def test_type_id(self):
        """ Checks if the attribute id is a str """
        obj = BaseModel()
        self.assertEqual(type(obj.id), str)

    def test_type_update_at(self):
        """ Checks if update_at is type datetime """
        obj = BaseModel()
        self.assertEqual(type(obj.updated_at), datetime.datetime)

    def test_type_created_at(self):
        """ Checks if created_at is type datetime """
        obj = BaseModel()
        self.assertEqual(type(obj.created_at), datetime.datetime)

    def test_before_todict(self):
        """Tests the instance before using the todict conversion"""
        obj = BaseModel()
        obj = obj.__dict__
        self.assertEqual(type(obj).__name__, "dict")
        self.assertTrue(hasattr(obj, '__class__'))
        self.assertEqual(str(obj.__class__),
                         "<class 'models.base_model.BaseModel'>")
        self.assertTrue(type(obj['created_at']), 'datetime.datetime')
        self.assertTrue(type(obj['updated_at']), 'datetime.datetime')
        self.assertTrue(type(obj['id']), 'str')

    def test_after_todict(self):
        """Tests instances after using to_dict conversion"""
        my_model = BaseModel()
        new_model = BaseModel()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, BaseModel)
        self.assertEqual(type(my_model).__name__, "BaseModel")
        self.assertEqual(test_dict['__class__'], "BaseModel")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)
