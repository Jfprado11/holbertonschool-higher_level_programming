#!/usr/bin/python3
"""Uniittest for bases
task 0
"""
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
        v1 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.assertEqual(Base.to_json_string(
            [v1]), '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')


if __name__ == '__main__':
    unittest.main()
