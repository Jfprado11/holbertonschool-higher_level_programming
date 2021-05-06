#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None
    len_str = len(sentence)
    first_char = sentence[0]
    tup = len_str, first_char
    return tup
