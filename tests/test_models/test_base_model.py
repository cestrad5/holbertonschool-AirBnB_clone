#!/usr/bin/python3
"""
Test for the base_model class
"""
from models.base_model import BaseModel
import unittest
import os
from datetime import datetime


class TestsBaseModel(unittest.TestCase):

    def test_save(self):
        b_1 = BaseModel()
        b_1.save()
        self.assertFalse(b_1.created_at == b_1.updated_at)

    def setUp(self):
        self.instanceOne = BaseModel()
        self.instanceTwo = BaseModel()

    def test_created_at(self):
        b_1 = BaseModel()
        self.assertTrue(type(b_1.created_at) == datetime)

    def testId(self):
        b_1 = BaseModel()
        b_2 = BaseModel()
        self.assertFalse(b_1.id == b_2.id)

    def testDict(self):
        b_1 = BaseModel()
        dictionary = {'id': b_1.id, 'created_at': b_1.created_at.isoformat(),
                      'update_at': b_1.updated_at.isoformat(),
                      '__class__': b_1.__class__.__name__}
        self.assertEqual(dictionary, b_1.to_dict())

    def testStr(self):
        b_1 = BaseModel()
        string_aux = f"[BaseModel] ({b_1.id}) {b_1.__dict__}"
        self.assertEqual(string_aux, str(b_1))


if __name__ == '__main__':
    unittest.main()
