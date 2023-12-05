#!/usr/bin/python3
"""Define class"""


class Student:
    """A class to represent a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            return {at: getattr(self, at) for at in attrs if hasattr(self, at)}
