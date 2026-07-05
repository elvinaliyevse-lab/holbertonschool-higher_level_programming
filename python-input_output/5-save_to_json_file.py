#!/usr/bin/python3
"""Module for saving Python objects to JSON files."""

from json import dumps


def save_to_json_file(my_obj, filename):
    """Save an object to a JSON file."""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
