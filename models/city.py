#!/usr/bin/python3
"""
Class Cityy inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class, inherits from BaseModel,
    contains public attributes, and use FileStorage
    system to do a correct serialization and deserialization
    """
    state_id = ""
    name = ""
