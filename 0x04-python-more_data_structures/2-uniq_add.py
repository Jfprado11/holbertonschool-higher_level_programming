#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    suma = 0
    new_list = list(new_list)
    for x in range(len(new_list)):
        suma += new_list[x]
    return suma
