#!/usr/bin/python3
"""BaseModel: defines all common attributes/methods for other classes."""


from datetime import datetime
import models
import uuid

class BaseModel:
    """BaseModel for the AirBnB clone"""

    def __init__(self, *args, **kwargs):
        """Creating a new BaseModel with defined args"""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
            """k and v for key and value"""
                if k in ["created_at", "updated_at"]:
                    v = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if k not in ['__class__']:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)
            self.save()

