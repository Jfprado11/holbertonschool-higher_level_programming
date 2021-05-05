#!/usr/bin/python3
def element_at(my_list, idx):
    lenList = len(my_list)
    if idx < 0:
        return None
    elif idx +1 > lenList:
        return None
    else:
        return my_list[idx]
