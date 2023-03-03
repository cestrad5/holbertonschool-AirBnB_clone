#!/usr/bin/python3
"""
This Module contains the class Amenity
inherits from class BaseModel
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    define Amenity

        attribute:
            name: the name of the amenity
    """
    name = ""
