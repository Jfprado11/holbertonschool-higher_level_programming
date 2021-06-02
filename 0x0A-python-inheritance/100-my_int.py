#!/usr/bin/python3
"""Changing some methods
insede a a int obj
"""


class MyInt(int):
    """a class that iherates from a int"""

    def __eq__(self, other):
        """change the equal function"""
        return int(self) != int(other)

    def __ne__(self, other):
        """change the diferent method"""
        return int(self) == int(other)
