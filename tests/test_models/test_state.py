#!/usr/bin/python3
"""
Unittest for state
"""


from models.state import State
import pep8
import os
import unittest


class Test_State(unittest.TestCase):
    """
    Unittest for the class State
    """

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/State.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """Checks if the docstring exists for each method and constructor"""
        self.assertTrue(len(State.__doc__) > 1)
        self.assertTrue(len(State.__init__.__doc__) > 1)
        self.assertTrue(len(State.__str__.__doc__) > 1)
        self.assertTrue(len(State.save.__doc__) > 1)
        self.assertTrue(len(State.to_dict.__doc__) > 1)

    def test_str_method(self):
        """Tests to see if each method is printing accurately"""
        obj = State()
        objprinted = obj.__str__()
        self.assertEqual(objprinted,
                         "[State] ({}) {}".format(obj.id, obj.__dict__))

    def test_before_todict(self):
        """Tests instances before using to_dict conversion"""
        obj = State()
        obj_dict = obj.__dict__
        self.assertEqual(type(obj).__name__, "State")
        self.assertTrue(hasattr(obj, '__class__'))
        self.assertEqual(str(obj.__class__),
                         "<class 'models.state.State'>")
        self.assertTrue(type(obj_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(obj_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(obj_dict['id']), 'str')

    def test_after_todict(self):
        """Test instances after using to_dict conversion"""
        my_model = State()
        new_model = State()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, State)
        self.assertEqual(type(my_model).__name__, "State")
        self.assertEqual(test_dict['__class__'], "State")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_hasattribute(self):
        """Tests if the instance of BaseModel has been correctly made"""
        obj = State()
        self.assertTrue(hasattr(obj, "__init__"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "id"))
