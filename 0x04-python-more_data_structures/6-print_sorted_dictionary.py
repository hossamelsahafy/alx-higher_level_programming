#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary == []:
        return None
    else:
        for i in sorted(a_dictionary):
            print("{}: {}".format(i, a_dictionary[i]))
