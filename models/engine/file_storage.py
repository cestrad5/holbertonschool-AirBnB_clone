#!/usr/bin/python3
"""This module contains the class File Storage"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    This class serializes and deserializes
    instances to a JSON"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        """Add new obj to existing dictionary of instances"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects """
        nDict = {k: v.to_dict() for k, v in self.all().items()}
        with open(FileStorage.__file_path, mode="w+", encoding="utf-8") as f:
            f.write(json.dumps(nDict))

    def reload(self):
        """ Deserializes the JSON file """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                l_dict = f.read()
                py_obj = json.loads(l_dict)
                FileStorage.__objects = {k: eval(
                    f"{v['__class__']}(**{v})") for k, v in py_obj.items()}
