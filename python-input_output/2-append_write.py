#!/usr/bin/python3
"""Module for appending a string to a text file."""

def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
