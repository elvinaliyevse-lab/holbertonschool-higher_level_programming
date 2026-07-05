#!/usr/bin/python3
"""Module containing add_attribute function"""


def add_attribute(obj, name: str, val: str):
    """Function to add attribute to an object"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    return setattr(obj, name, val)
