#!/usr/bin/python3
count = 122
while (count >= 97):
    if (count % 2 == 0):
        num = count
    else:
        num = count - 32
    count = count - 1
    print("{}".format(chr(num)), end="")
