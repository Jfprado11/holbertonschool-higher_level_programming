#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = sorted(list(a_dictionary))
    for hey in new_list:
        print("{} : {}".format(hey, a_dictionary[hey]))
