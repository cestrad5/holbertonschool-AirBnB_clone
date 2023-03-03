#!/usr/bin/python3
'''
FileStore class test
'''
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestsFileStorage(unittest.TestCase):

    def setUp(self):
        self.file1 = FileStorage()
        self.obj1 = BaseModel()

    def test_new(self):
        self.assertTrue(self.file1._FileStorage__objects.get(
            f"BaseModel.{self.obj1.id}"))

    def test_file_path(self):
        self.assertTrue(self.file1.FileStorage__file_path == "file.json")

    def test_all(self):
        self.assertTrue(self.file1.all().get(f"BaseModel.{self.obj1.id}"))

    def test_save(self):
        self.obj1.save()
        self.assertTrue(self.file1._FileStorage__objects.get(
            f"BaseModel.{self.obj1,id}"))

    def test_reload(self):

        if os.path.exists('file.json'):
            self.file1.reload()
            self.assertEqual(len(self.file1._FileStorage__objects), 0)


if __name__ == '__main__':
    unittest.main()
