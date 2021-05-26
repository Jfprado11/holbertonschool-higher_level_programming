#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """checks all posible cases for task 6
    """
    def test_max_number(self):
        """check the max number of a list"""
        self.assertEqual(max_integer([1, 5, -8, 3, 8]), 8)
        self.assertEqual(max_integer([-8,-55555, -4444, -555]), -8)
        self.assertEqual(max_integer([1, 2, 4, 5]), 5)
        self.assertEqual(max_integer([44444444, 55555, 888888]), 44444444)

    def test_empty(self):
        """check the correct ouput for a list"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_fails(self):
        """check the type of errors"""
        with self.assertRaises(TypeError):
            max_integer([1, "hola"])
            max_integer([1, [1, 3]])
            max_integer([1, 2, 4.5])
            max_integer(True)
            max_integer("jhkdd")

    def test_docmodule(self):
        """test if have module documentation"""
        temp = __import__('6-max_integer').__doc__
        self.assertTrue(temp is not None and len(temp) > 4)

    def test_docfunction(self):
        """test if have function documentation"""
        temp = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(temp is not None and len(temp) > 4)
