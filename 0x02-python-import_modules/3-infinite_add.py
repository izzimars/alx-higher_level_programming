#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    ls = arguments[1:]
    sum = 0

    for j in ls:
        sum = sum + int(j)
    print("{}".format(sum))
