#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test the method of max int"""

    def test_maxInt(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([7, 2, 3, 3]), 7)
        self.assertEqual(max_integer([7, 2, 10, 3]), 10)
        self.assertEqual(max_integer([7, 7, 3]), 7)
        self.assertEqual(max_integer([-9, -7, -3]), -3)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([1, 2, -3]), 2)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_error_checks(self):
        with self.assertRaises(TypeError):
            max_integer([1, "juan"])
            max_integer("hola")

