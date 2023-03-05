#!/usr/bin/python3

"""Unittest BaseModel class"""

from datetime import datetime
import unittest
import os
from models.base_model import BaseModel
#from models import base_model


class TEST_base(unittest.TestCase):

    @classmethod
    def setup(self):
        self.base1 = BaseModel()
        self.name = "John Smith"
        self.base1.my_number = 25

    @classmethod
    def tearDown(self):
        del self.base1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_atritt(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "save"))

    def test_to_dict(self):
        base = BaseModel()
        base.name = "Alex"
        base.age = 22
        convert = base.to_dict()
        self.assertEqual(convert["id"], base.id)
        self.assertEqual(convert["name"], base.name)
        self.assertEqual(convert["age"], base.age)
        self.assertEqual(convert["updated_at"], base.updated_at.isoformat())
        self.assertEqual(convert["created_at"], base.created_at.isoformat())
        self.assertEqual(convert["__class__"], type(base).__name__)

    def tets_save(self):
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def test_functions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)


if __name__ == "__main__":
    unittest.main()
