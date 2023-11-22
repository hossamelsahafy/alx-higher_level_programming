#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """relative position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of the square"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """print square with #"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print(
                "\n".join(
                    " " * self.__position[0] + "#" * self.__size
                    for _ in range(self.__size)
                )
            )
