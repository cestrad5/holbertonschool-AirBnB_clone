#!/usr/bin/python3
"""
This Module contains the class city
inherits from class BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """define city
        attribute:
            state_id: state
            name: the name of the city
    """

    state_id = ""
    name = ""
