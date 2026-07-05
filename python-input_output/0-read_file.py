#!/usr/bin/python3
"""Read the contents of a text file and print them to stdout."""


def read_file(filename=""):
    """Read a file and print its contents."""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
