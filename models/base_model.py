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

    def __str__(self):
        """ String Representation of BaseModel """
        class_name = self.__class__.__name__
        string = ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
        return string

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Rreturns a dictionary containing all keys/values of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return(my_dict)