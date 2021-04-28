#!/usr/bin/python3
def print_last_digit(number):
    n = abs(number)
    n = n % 10
    print("{:d}".format(n), end="")
    return n
