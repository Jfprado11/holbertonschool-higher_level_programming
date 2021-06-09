#!/usr/bin/python3
"""Tests cases for the class
square
"""

from models.base import Base
from models.square import Square
import unittest
from unittest import mock
from unittest.mock import patch
from models.rectangle import Rectangle
import io


class TestSquareClass(unittest.TestCase):
    """a class to check some cases in class square"""

    def setUp(self):
        """the setup of the class cases"""
        Base._Base__nb_objects = 0

    def test_id_rectangle(self):
        """the test fot the rectangle"""
        s1 = Square(2)
        self.assertEqual(s1.id, 1)
        s2 = Square(1, 3, 4, 6)
        self.assertEqual(s2.id, 6)
        s3 = Square(3)
        self.assertEqual(s3.id, 2)

    def test_posibles_errors(self):
        """checking if the user tries to enter the
         privates value return error"""
        b3 = Square(1, 2, 5, 6)
        with self.assertRaises(AttributeError):
            b3.__x
            b3.__y

    def test_str_square(self):
        """testing the output of the string"""
        s1 = Square(3)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 3")
        s2 = Square(3, 6, 5)
        self.assertEqual(s2.__str__(), "[Square] (2) 6/5 - 3")
        s2 = Square(3, 6, 5, 10)
        self.assertEqual(s2.__str__(), "[Square] (10) 6/5 - 3")
        s2 = Square(5)
        self.assertEqual(s2.__str__(), "[Square] (3) 0/0 - 5")

    def test_error_square(self):
        """testing the raising errors"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            b1 = Square("hello", 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            b3 = Square(1, "hello", 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            b4 = Square(5, 2, "hello")

    def test_raising_ValueError(self):
        """check if we put some value less than
        raise a ValueError """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            b1 = Square(-1, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            b1 = Square(1, -2, 3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            b1 = Square(1, 2, -1)

    def test_update_square(self):
        """using the square for the square"""
        s1 = Square(5)

        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")


if __name__ == '__main__':
    unittest.main()
