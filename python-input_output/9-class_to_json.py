#!/usr/bin/python3
"""Module for converting an object to a JSON-serializable dictionary."""

def class_to_json(obj):
    return obj.__dict__
