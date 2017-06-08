#!/usr/bin/env python3

"""FizzBuzz programming exercise"""


def fizz_buzz_assess():
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        if i % 3 == 0:
            print("Fizz")
        if i % 5 == 0:
            print("Buzz")
        else:
            print(i)

print(__name__)
