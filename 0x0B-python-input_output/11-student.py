#!/usr/bin/python3
"""define class"""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiates a Student object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            return {at: getattr(self, at) for at in attrs if hasattr(self, at)}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
