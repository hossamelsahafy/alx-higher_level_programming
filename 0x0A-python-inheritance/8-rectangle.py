#!/usr/bin/python3
"""
Define class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Define Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
