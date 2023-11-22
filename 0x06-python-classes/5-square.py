#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square."""
        self.size = size

    @property
    def size(self):
        """set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, ensuring it is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """print square with #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
