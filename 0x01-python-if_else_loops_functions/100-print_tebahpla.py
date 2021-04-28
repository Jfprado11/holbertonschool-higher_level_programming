#!/usr/bin/python3
result = ""
for i in reversed(range(97, 123)):
    if (i % 2) == 0:
        result += chr(i)
    elif (i % 2) == 1:
        result += chr(i - 32)
print("{:s}".format(result))
