#!/usr/bin/python3
"""Module for inserting text after matching lines in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a string after each line containing a search string."""
    with open(filename, mode='r', encoding='utf-8') as f:
        text = f.readlines()
        new_text = []

        for line in text:
            new_text.append(line)

            if search_string in line:
                new_text.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as nf:
        for line in new_text:
            nf.write(line)
