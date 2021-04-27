#!/usr/bin/python3
for j in range(10):
    for i in range(10):
        if (j != i) and (j < i) and ((j * 10) + i) < 89:
            print("{:d}{:d}".format(j, i), end=", ")
        elif ((j * 10) + i) == 89:
            print("{:d}{:d}".format(j, i), end="")
print()
