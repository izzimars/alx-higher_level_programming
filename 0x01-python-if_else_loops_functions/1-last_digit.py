#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numlst = int((str(number))[-1])
if (number < 0):
    numlst = numlst * -1
if (numlst > 6):
    print("Last digit of", number, "is", numlst, "and is greater than 5")
elif (numlst == 0):
    print("Last digit of", number, "is", numlst, "and is 0")
else:
    print("Last digit of", number, "is", numlst, "and is less than 6 and not 0")

