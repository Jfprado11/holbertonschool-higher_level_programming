#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    len_list = len(my_list)
    if len_list < 0 or idx + 1 > len_list:
        return my_list
    del my_list[idx]
    return my_list
