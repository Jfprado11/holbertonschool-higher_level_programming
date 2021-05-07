#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_lists = list(sorted(a_dictionary.keys()))
    for hey in new_lists:
        print(hey, ":", a_dictionary[hey])
