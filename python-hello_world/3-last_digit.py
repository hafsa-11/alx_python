#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

print("Last digit of {} is {} and is ".format(number, -last_digit if number < 0 else last_digit), end="")

if last_digit == 0 and number != 0:
    print("0")
elif number < 0:
    print("less than 6 and not 0")
else:
    print("greater than 5" if number != 0 else "0")