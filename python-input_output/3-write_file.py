#!/usr/bin/python3
"""Module for writing a string to a text file."""

def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
