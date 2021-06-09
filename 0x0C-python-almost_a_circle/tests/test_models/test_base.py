#!/usr/bin/python3
"""Uniittest for bases
task 0
"""
from models.rectangle import Rectangle
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test all posible cases for the
    class base
    """

    def test_id_base(self):
        """test if the output is correct
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(4)
        self.assertEqual(b2.id, 4)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_json_string(self):
        """checking if a string in json is retriving"""
        r1 = Rectangle(10, 7, 2, 8)
        v1 = r1.to_dictionary()
        self.assertEqual(Base.to_json_string(
            [v1]), '[{"width": 10, "height": 7, "x": 2, "y": 8, "id": 3}]')


if __name__ == '__main__':
    unittest.main()
