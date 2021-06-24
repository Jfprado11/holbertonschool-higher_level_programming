#!/usr/bin/python3
"""Uniittest for bases
task 0
"""
from models.base import Base
import unittest
from unittest import mock
from unittest.mock import patch
from models.rectangle import Rectangle
import io


class TestRectangleClass(unittest.TestCase):
    """Test all posible cases for the
    class base
    """

    def setUp(self):
        """the setup of the classes of the test cases"""
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
            b1 = Rectangle(0, 3)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            b1 = Rectangle(2, -2)
            b1 = Rectangle(2, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            b1 = Rectangle(1, 2, -2, 3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            b1 = Rectangle(1, 2, 5, -1)

    def test_area_rectangle(self):
        """check if the area of the rectangle is correct"""
        r1 = Rectangle(3, 3)
        self.assertEqual((r1.area()), 9)
        r2 = Rectangle(5, 8, 9, 2, 5)
        self.assertEqual(r2.area(), 40)
        r3 = Rectangle(1, 1)
        self.assertEqual(r3.area(), 1)

    def test_draw_recntangle(self):
        """testing if the stdout is correct or not"""
        a = "###\n###\n###\n"
        r1 = Rectangle(3, 3)
        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as stdo:
            r1.display()
        self.assertEqual(stdo.getvalue(), a)
        a = "####\n####\n####\n####\n####\n####\n"
        r2 = Rectangle(4, 6)
        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as stdo:
            r2.display()
        self.assertEqual(stdo.getvalue(), a)

    def test_str_recntalge(self):
        """testing if the output in str is correct"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(2, 5)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 0/0 - 2/5")
        r3 = Rectangle(5, 6, 7, 8)
        self.assertEqual(r3.__str__(), "[Rectangle] (2) 7/8 - 5/6")

    def test_display_1(self):
        """testing if the input has a correct value"""
        a = "\n\n  ##\n  ##\n  ##\n"
        r1 = Rectangle(2, 3, 2, 2)
        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as stdo:
            r1.display()
        self.assertEqual(stdo.getvalue(), a)
        a = " ###\n ###\n"
        r2 = Rectangle(3, 2, 1, 0)
        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as stdo:
            r2.display()
        self.assertEqual(stdo.getvalue(), a)

    def test_update_0(self):
        """testing if the updates worked as expected"""
        r1 = Rectangle(2, 2, 2, 2, 2)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 2/2 - 2/2")

        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 2/2 - 2/2")

        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 2/2 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/2 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_1(self):
        """checking update 1 with some cases"""
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    def test_dict_rectangle(self):
        """checking if the dictionary prints correctly"""
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.to_dictionary(), {
                         'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        r2 = Rectangle(8, 9)
        self.assertEqual(r2.to_dictionary(), {
                         'x': 0, 'y': 0, 'id': 2, 'height': 9, 'width': 8})


if __name__ == '__main__':
    unittest.main()
