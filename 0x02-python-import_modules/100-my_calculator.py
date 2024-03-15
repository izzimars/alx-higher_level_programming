#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, div, mul, sub

    arguments = sys.argv
    ls = arguments[1:]
    
    if (len(ls) != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(ls[0])
    b = int(ls[2])

    if (ls[1] not in ["-", "+", "*", "/"]):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif (ls[1] == '+'):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif (ls[1] == '-'):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif (ls[1] == '*'):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
