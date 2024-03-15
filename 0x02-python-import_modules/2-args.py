#!/usr/bin/python3
import sys

arguments = sys.argv
ls = arguments[1:]
i = 1
if len(ls) == 0:
    print("0 arguments.")
else:
    if (len(ls) == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(len(ls)))
    for j in ls:
        print("{}: {}".format(i, j))
        i = i + 1
