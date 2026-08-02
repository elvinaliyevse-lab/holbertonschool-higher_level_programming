#!/usr/bin/python3
"""Defines a class locking the creation of new instance attributes"""


class LockedClass:
    """Only allows the first_name instance attribute to be created"""

    __slots__ = ["first_name"]
