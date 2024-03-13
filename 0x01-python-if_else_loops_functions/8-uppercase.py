#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) >= 97 and ord(i) < 123):
            num = ord(i) - 32
        else:
            num = ord(i) - 0
        print("{}".format(chr(num)), end="")
    print()
