#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = ()
    j = len(tuple_a)
    i = len(tuple_b)
    tup1 = ((tuple_a[0] if j > 0 else 0) + (tuple_b[0] if i > 0 else 0))
    tup2 = ((tuple_a[1] if j > 1 else 0) + (tuple_b[1] if i > 1 else 0))
    res = tup1, tup2
    return(res)
