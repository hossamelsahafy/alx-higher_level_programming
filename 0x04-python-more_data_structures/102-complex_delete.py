#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_key = [key for key, val in a_dictionary.items() if val == value]
    for key in delete_key:
        del a_dictionary[key]
    return a_dictionary
