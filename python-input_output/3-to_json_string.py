#!/usr/bin/python3
"""Module for converting Python objects to JSON strings."""

from json import dumps


def to_json_string(my_obj):
    """Return the JSON representation of an object."""
    return dumps(my_obj)
