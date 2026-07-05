#!/usr/bin/python3
"""Module defining the Student class for serialization."""


class Student:
    """Represent a student with a first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the student."""
        return self.__dict__
