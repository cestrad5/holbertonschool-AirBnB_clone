#!/usr/bin/python3
"""
unit test for Review class
"""
from unittest import TestCase
from models.review import Review


class StateTest(TestCase):
    """ test case class for Review class """

    def setUp(self):
        """ setting up basic object """
        self.review = Review()

    def tearDown(self):
        """ safely deleting the object """
        del self.review

    def test_type(self):
        """ checks the type of the attribute """
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_attr(self):
        """ tests if the given attribute exists """
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))


if __name__ == '__main__':
    unittest.main()
