#!/usr/bin/python3
"""Module for converting JSON strings to Python objects."""

from json import loads


def from_json_string(my_str):
    return loads(my_str)
