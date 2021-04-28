#!/usr/bin/python3
def main():
    from sys import argv
    summ = 0
    for i in range(1, len(argv)):
        summ += int(argv[i])
    print(summ)

if __name__ == "__main__":
    main()
