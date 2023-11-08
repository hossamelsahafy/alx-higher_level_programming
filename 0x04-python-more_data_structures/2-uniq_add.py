#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list == "":
        return None
    else:
        return (sum(set(my_list)))
