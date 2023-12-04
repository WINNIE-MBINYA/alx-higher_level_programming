#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in range(len(matrix)):
        for n in range(len(matrix[r])):
            if n != 0:
                print(" ", end='')
            print("{:d}".format(matrix[r][n]), end='')
        print()
