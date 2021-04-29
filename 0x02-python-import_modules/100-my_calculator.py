#!/usr/bin/python3
def main():
    from calculator_1 import add, sub, mul, div
    import sys
    av = sys.argv
    lenAv = len(sys.argv)
    if lenAv != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if av[2] != '+' and av[2] != '-' and av[2] != '*' and av[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(av[1])
    b = int(av[3])
    if av[2] == '+':
        print(a, av[2], b, "=", add(a, b))
    if av[2] == '-':
        print(a, av[2], b, "=", sub(a, b))
    if av[2] == '*':
        print(a, av[2], b, "=", mul(a, b))
    if av[2] == '/':
        print(a, av[2], b, "=", div(a, b))

if __name__ == "__main__":
    main()
