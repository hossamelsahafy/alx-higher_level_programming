#!/usr/bin/python3
"""
Define class
"""


Rectangle = __import__("9-base_geometry").BaseGeometry


class Square(Rectangle):
    """Define Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size**2
