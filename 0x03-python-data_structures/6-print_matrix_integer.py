#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print('\n'.join([' '.join(['{:d}'.format(j) for j in k])for k in matrix]))
