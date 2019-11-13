#!/usr/bin/python3
"""
Class State inherits from BaseModel class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class, inherits from BaseModel, contains public attribute, and use FileStorage
    system to do a correct serialization and deserialization
    """
    name = ""
