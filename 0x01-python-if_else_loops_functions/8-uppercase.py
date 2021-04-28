#!/usr/bin/python3
def uppercase(str):
    result = ""
    for low in str:
        low = ord(low)
        if (low >= 97) and (low <= 122):
            result += chr(low - 32)
        else:
            result += chr(low)
    print("{:s}".format(result))
