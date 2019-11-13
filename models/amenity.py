#!/usr/bin/python3
"""
Class Amenityy inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class, inherits from BaseModel,
    contains public attributes, and use FileStorage
    system to do a correct serialization and deserialization
    """
    name = ""
