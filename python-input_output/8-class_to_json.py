#!/usr/bin/python3
"""Module for converting an object to a JSON-serializable dictionary."""


def class_to_json(obj):
    """Return a dictionary representation of an object's attributes."""
    return obj.__dict__
