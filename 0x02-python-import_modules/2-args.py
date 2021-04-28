#!/usr/bin/python3
def main():
    from sys import argv
    lenArgv = len(argv)
    if lenArgv == 2:
        print("{:d} argument:".format(lenArgv - 1))
    elif lenArgv <= 1:
        print("{:d} arguments.".format(lenArgv - 1))
    else:
        print("{:d} arguments:".format(lenArgv - 1))
    for i in range(1, lenArgv):
        print("{:d}: {:s}".format(i, argv[i]))

if __name__ == "__main__":
    main()
