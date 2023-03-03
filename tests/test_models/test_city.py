#!/usr/bin/python3
""" This is the Unittest for class City """

import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def test_city_name(self):

        city_x = City()
        self.assertTrue(hasattr(city_x, 'name'))
        self.assertEqual(city_x.name, "")
        city_x.name = "London"
        self.assertEqual(city_x.name, "London")

    def test_city_state_id(self):

        city_x = City()
        self.assertTrue(hasattr(city_x, 'state_id'))
        self.assertEqual(city_x.state_id, "")
        city_x.state_id = "123456"
        self.assertEqual(city_x.state_id, "123456")
