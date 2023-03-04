#!/usr/bin/python3
"""
unit test for State class
"""
from unittest import TestCase
from models.state import State


class StateTest(TestCase):
    """ test case class for State class """

    def setUp(self):
        """ setting up basic object """
        self.state = State()

    def tearDown(self):
        """ safely deleting the object """
        del self.state

    def test_type(self):
        """ checks the type of the attribute """
        self.assertIsInstance(self.state.name, str)

    def test_attr(self):
        """ tests if the given attribute exists """
        self.assertTrue(hasattr(self.state, 'name'))


if __name__ == '__main__':
    unittest.main()
