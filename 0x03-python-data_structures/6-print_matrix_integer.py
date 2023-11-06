#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for r in matrix:
            for i in range(len(r)):
                if i < len(r) - 1:
                    print("{:d}".format(r[i]), end=' ')
            else:
                print("{:d}".format(r[i]))
