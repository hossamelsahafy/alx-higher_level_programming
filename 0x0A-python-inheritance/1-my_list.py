#!/usr/bin/python3
"""
Define class
"""


class MyList(list):
    """Define MyList class"""

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Define function that print sorted list"""
        print(sorted(self))
