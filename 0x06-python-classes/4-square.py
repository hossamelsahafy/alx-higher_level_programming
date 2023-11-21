#!/usr/bin/python3

"""Define the Square."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize a square with a given size."""
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area for square"""
        return self.__size * self.__size
