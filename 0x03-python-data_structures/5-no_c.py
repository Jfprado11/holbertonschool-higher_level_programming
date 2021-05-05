#!/usr/bin/python3
def no_c(my_string):
    count_lower_C = my_string.count("c")
    count_upper_C = my_string.count("C")
    if count_lower_C > 0:
        my_string = list(my_string)
        while count_lower_C:
            my_string.remove("c")
            count_lower_C -= 1
        my_string = "" .join(my_string)
    if count_upper_C > 0:
        my_string = list(my_string)
        while count_upper_C:
            my_string.remove("C")
            count_upper_C -= 1
        my_string = "".join(my_string)
    return my_string
