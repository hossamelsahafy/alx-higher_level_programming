#!/usr/bin/python3

"""Define the Square."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize a square with a given size.
        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
