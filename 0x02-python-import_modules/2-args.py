#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    def print_args():
        n_args = len(sys.argv) - 1
        if n_args == 0:
            print("0 arguments")
        elif n_args == 1:
            print("1 argument:")
            print("1: {}".format(sys.argv[1]))
        else:
            print("{} arguments:".format(n_args))
            for i in range(1, len(sys.argv)):
                print("{}: {}".format(i, sys.argv[i]))
    print_args()
