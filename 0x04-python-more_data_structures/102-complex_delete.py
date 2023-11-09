#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    return {key: i for key, i in a_dictionary.items() if i != value}
