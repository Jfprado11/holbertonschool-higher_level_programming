#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_lists = sorted(list(a_dictionary))
    for hey in new_lists:
        print(hey, ":", a_dictionary[hey])
