#!/usr/bin/python3
"""Module for converting Python objects to JSON strings."""

from json import dumps


def to_json_string(my_obj):
    return dumps(my_obj)
