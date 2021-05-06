#!/usr/bin/python3
def multiple_returns(sentence):
    len_str = len(sentence)
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]
    tup = len_str, first_char
    return tup
