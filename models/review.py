#!/usr/bin/python3
"""
Class Revieww inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class, inherits from BaseModel,
    contains public attributes, and use FileStorage
    system to do a correct serialization and deserialization
    """
    place_id = ""
    user_id = ""
    text = ""
