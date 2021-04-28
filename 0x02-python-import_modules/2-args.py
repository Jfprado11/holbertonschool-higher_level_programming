#!/usr/bin/python3
def main():
    import sys
    lenArgv = len(sys.argv)
    if lenArgv == 2:
        print(lenArgv - 1, "argument:")
    elif lenArgv <= 1:
        print(lenArgv - 1, "arguments.")
    else:
        print(lenArgv - 1, "arguments:")
    for i in range(1, lenArgv):
        print(i, ":", sys.argv[i])

if __name__ == "__main__":
    main()
