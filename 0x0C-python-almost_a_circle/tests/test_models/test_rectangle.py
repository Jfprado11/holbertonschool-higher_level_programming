#!/usr/bin/python3
"""Uniittest for bases
task 0
"""
from models.base import Base
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test all posible cases for the
    class base
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_rectangle(self):
        """testing if the id's are correctly output"""
        b1 = Rectangle(4, 2)
        self.assertEqual(b1.id, 1)
        b2 = Rectangle(1, 2, 5, 5, 12)
        self.assertEqual(b2.id, 12)
        b3 = Rectangle(1, 4, 6, 7)
        self.assertEqual(b3.id, 2)
        b4 = Rectangle(1, 6, 7, 9)
        self.assertEqual(b4.id, 3)

    def test_posibles_errors(self):
        """checking if the user tries to enter the
         privates value return error"""
        b3 = Rectangle(1, 2, 5, 6)
        with self.assertRaises(AttributeError):
            b3.__width
            b3.__height

    def test_raising_TypeError(self):
        """checking if it raises when it
        pases erros"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            b1 = Rectangle("hello", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            b2 = Rectangle(2, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            b3 = Rectangle(1, 2, "hello", 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            b4 = Rectangle(5, 2, 3, "hello")

    def test_raising_ValueError(self):
        """check if we put some value less than
        raise a ValueError """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            b1 = Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            b1 = Rectangle(2, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            b1 = Rectangle(1, 2, -2, 3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            b1 = Rectangle(1, 2, 5, -1)


if __name__ == '__main__':
    unittest.main()
