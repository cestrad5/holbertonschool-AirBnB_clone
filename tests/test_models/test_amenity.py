#!/usr/bin/python3
"""
This is the Unittest for class Amenity
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_amenity_name(self):
        review = Amenity()
        self.assertTrue(hasattr(review, 'name'))
        self.assertEqual(review.name, "")
        review.name = "This is a review of a great place"
        self.assertEqual(review.name, "This is a review of a great place")
