#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_list2 = []
    for x in my_list:
        if ((x % 2) == 0):
            div_list2.append(True)
        else:
            div_list2.append(False)
    return div_list2
