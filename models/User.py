#!/usr/bin/python3
"""
Class User inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class, inherits from BaseModel, contains public attributes, and use FileStorage
    system to do a correct serialization and deserialization
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
