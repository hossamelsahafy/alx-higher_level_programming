#!/usr/bin/python3
"""
Define function
"""


def inherits_from(obj, a_class):
    """that checks if an object is an instance of a class that \
        inherited (directly or indirectly) from the specified class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
