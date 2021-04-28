#!/usr/bin/python3
for i in reversed(range(97, 123)):
    print("{:c}".format(i -32 if i % 2 == 1 else i), end="")
