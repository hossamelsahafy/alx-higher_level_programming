#!/usr/bin/python3
"""
Define class
"""


class BaseGeometry:
    """Define BaseGeometry class"""

    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Define integer_validator function"""
        if not isinstance(name, str):
            raise TypeError("{} must be a string".format(name))
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
