#!/usr/bin/python3
"""
unit test for City class
"""
from unittest import TestCase
from models.city import City


class CityTest(TestCase):
    """ test case class for City class """

    def setUp(self):
        """ setting up basic object """
        self.city = City()

    def tearDown(self):
        """ safely deleting the object """
        del self.city

    def test_type(self):
        """ checks the type of the attribute """
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_attr(self):
        """ tests if the given attribute exists """
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))


if __name__ == '__main__':
    unittest.main()
