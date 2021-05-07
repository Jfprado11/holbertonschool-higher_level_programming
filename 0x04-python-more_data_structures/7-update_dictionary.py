#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for hey in list(a_dictionary):
        if hey == key:
            a_dictionary[hey] = value
        a_dictionary[key] = value
    return a_dictionary
