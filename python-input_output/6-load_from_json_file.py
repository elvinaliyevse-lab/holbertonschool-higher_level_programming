#!/usr/bin/python3
"""Module for loading Python objects from JSON files."""

from json import loads


def load_from_json_file(filename):
    """Load an object from a JSON file."""
    with open(filename, encoding='utf-8') as f:
        return loads(f.read())
