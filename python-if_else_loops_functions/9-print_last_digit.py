#!/usr/bin/python3
def print_last_digit(number):
    """Print and return the last digit of a number."""
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last
