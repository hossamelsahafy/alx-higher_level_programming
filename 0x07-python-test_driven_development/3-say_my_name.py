#!/usr/bin/python3
"""Define function that prints name"""


def say_my_name(first_name, last_name=""):
    """
    define function that print names
    """
    if not isinstance(first_name, str) or first_name == "":
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
