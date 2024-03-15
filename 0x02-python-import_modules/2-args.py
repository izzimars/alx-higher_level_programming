#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    ls = arguments[1:]
    i = 1

    if len(ls) == 0:
        print("{} arguments.".format(len(ls)))
    else:
        if (len(ls) == 1):
            print("{} argument:".format(len(ls)))
        else:
            print("{} arguments:".format(len(ls)))
        for j in ls:
            print("{}: {}".format(i, j))
            i = i + 1
