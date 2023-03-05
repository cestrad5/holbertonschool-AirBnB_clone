#!/usr/bin/python3
"""
Review Module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class inherits from BaseModel

    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ initializes parent class """
        if args and type(args[0]) is dict:
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)
