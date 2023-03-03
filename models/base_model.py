#!/usr/bin/python3
"""
Class BaseModel that defines all common
attributes/methods for other classes
"""

#import models
import uuid
"""
UUID = Universally Unique Identifiers
The goal is to have unique id for each BaseModel
"""
from datetime import datetime


class BaseModel:
    """
    This class defines all common attributes for a model
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        Args:
            - args: unused until now
            - kwargs: each key of this dictionary is an attribute name
        
        """

        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(self.created_at,
                                                '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(self.updated_at,
                                                '%Y-%m-%dT%H:%M:%S.%f')

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """

        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
    
    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """

        self.updated_at = datetime.now()
        storage.save()
