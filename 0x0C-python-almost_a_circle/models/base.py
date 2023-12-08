#!/usr/bin/python3
"""Define Base class"""


class Base:
    """Define  class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
