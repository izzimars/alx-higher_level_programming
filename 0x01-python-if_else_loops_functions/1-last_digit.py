#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number >= 0):
    lst = number % 10
if (number < 0):
    lst = number % -10
if (lst > 6):
    print("Last digit of", number, "is", lst, "and is greater than 5")
elif (lst == 0):
    print("Last digit of", number, "is", lst, "and is 0")
else:
    print("Last digit of", number, "is", lst, "and is less than 6 and not 0")
