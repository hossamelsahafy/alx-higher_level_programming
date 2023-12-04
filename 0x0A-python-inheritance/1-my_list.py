#!/usr/bin/python3
"""
Define class
"""


class MyList(list):
    """Define MyList class"""

    def print_sorted(self):
        """Define function that print sorted list"""
        print(sorted(self))
