#!/usr/bin/python3
"""
Init file that starts the models module
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
