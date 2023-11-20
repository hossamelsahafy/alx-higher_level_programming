#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except (IndexError, TypeError, NameError, ValueError) as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
    except ZeroDivisionError:
        res = None
        return None
    else:
        return res
