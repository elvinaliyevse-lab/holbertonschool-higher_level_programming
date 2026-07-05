#!/usr/bin/python3
"""Module containing MyInt class"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, __value: object):
        """Making reverse =="""
        return super().__ne__(__value)

    def __ne__(self, __value: object):
        """Making reverse !="""
        return super().__eq__(__value)
