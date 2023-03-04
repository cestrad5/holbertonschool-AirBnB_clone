#!/usr/bin/python3
"""
unit test for Amenity class
"""
from unittest import TestCase
from models.amenity import Amenity


class AmenityTest(TestCase):
    """ test case class for amenity class """

    def setUp(self):
        """ setting up basic object """
        self.am = Amenity()

    def tearDown(self):
        """ safely deleting the object """
        del self.am

    def test_type(self):
        """ checks the type of the attribute """
        self.assertIsInstance(self.am.name, str)

    def test_attr(self):
        """ tests if the given attribute exists """
        self.assertTrue(hasattr(self.am, 'name'))


if __name__ == '__main__':
    unittest.main()
