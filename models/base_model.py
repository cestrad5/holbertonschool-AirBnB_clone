#!/usr/bin/python3
"""
This is a class BaseModel that defines all common
attributes/methods for other classes
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """
    Base class for Airbnb clone project
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor:
        - Generate random uuid,
        - created_at and updated_at uses the method strptime() to convert
        the string representation to a datetime object
        - if the key is __class__ means that the key is not a
        class attribute
        - if kwargs is empty then generate a random identifier
        and set the corresponding values for created and updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a formatted string representation of an object
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        This method updates the updated_at with the TIME when it's called
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        This method will be the first piece of the
        serialization/deserialization process:
        create a dictionary representation with
        “simple object type” of our BaseModel
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        - __dict__ is a dictionary of attributes
        - __class__ is the class of the instance
        """
        temp_dict = self.__dict__.copy()
        temp_dict['__class__'] = self.__class__.__name__
        temp_dict['created_at'] = self.created_at.isoformat()
        temp_dict['updated_at'] = self.updated_at.isoformat()
        return temp_dict
