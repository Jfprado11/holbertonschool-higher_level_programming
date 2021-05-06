#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = [list(map(lambda x: x * x, x)) for x in matrix]
    return (new_list)
