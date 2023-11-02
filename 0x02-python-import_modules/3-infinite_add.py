#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def print_numbers():
        if len(sys.argv) == 1:
            print("0")
        else:
            t = sum(int(args) for args in sys.argv[1:])
            print(t)
    print_numbers()
