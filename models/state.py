#!/usr/bin/python3
"""
State Module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State class inherits from BaseModel

    Attributes:
        name: input name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ initializes parent class """
        if args and type(args[0]) is dict:
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)
