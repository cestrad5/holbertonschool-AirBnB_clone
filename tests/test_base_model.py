#!/usr/bin/python3
"""
Instantiating BaseModel.
"""
import unittest
from models.base_model import BaseModel
import pycodestyle
import datetime


class TestBaseModel(unittest.TestCase):
    """
    Testing functions.
    """

    def test_is_an_instance(self):
        """
        Checking with assertIsInstance
        """
        my_BaseModel = BaseModel()
        self.assertIsInstance(my_BaseModel, BaseModel)

    def test_attributes(self):
        """
        Checking with hasattr attributes
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_id(self):
        """
        It is generating unique IDs?
        """
        my_BaseModel_1 = BaseModel().id
        my_BaseModel_2 = BaseModel().id
        self.assertNotEqual(my_BaseModel_1, my_BaseModel_2)

    def test_save(self):
        """
        Check if the class save the update the date
        """
        B_time = BaseModel()
        time_1 = B_time.updated_at
        sleep(.2)
        B_time.save()
        time_2 = B_time.updated_at
        self.assertNotEqual(time_1, time_2)

    def test_to_dict(self):
        """
        Test to dict
        """
        my_BaseModel = BaseModel()
        my_dict = my_BaseModel.to_dict()
        self.assertIs(type(my_dict), dict)
        self.assertIs(type(my_dict['created_at']), str)
        self.assertIs(type(my_dict['updated_at']), str)

    def test_style(self):
        """
        Check if the file had correct style
        """
        pstyle = pycodestyle.StyleGuide(quiet=True)
        result = pstyle.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors.")

    def test_user_updated(self):
        """test to check user updated_at"""
        User_1 = BaseModel()
        self.assertEqual(type(User_1.updated_at), type(datetime.now()))
        self.assertTrue(hasattr(User_1, "updated_at"))

    @classmethod
    def tearDownClass(cls):
        """
        Clear testing enviroment
        """
        print('\n****************** Finish Testing ******************\n')
        ...


if __name__ == '__main__':
    unittest.main()
