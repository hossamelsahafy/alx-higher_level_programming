#!/usr/bin/python3

"""Define the Square."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize a square with a given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of square"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value

    def area(self):
        """return the current area for square """
        return self.__size * self.__size
