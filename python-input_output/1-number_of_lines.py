#!/usr/bin/python3
"""Module for counting lines in a text file."""

def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as f:
        return len(f.readlines())
