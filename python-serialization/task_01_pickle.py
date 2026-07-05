#!/usr/bin/python3
"""Pickle-based object serialization helpers."""

import pickle


class CustomObject:
    """A simple custom object that can be pickled and unpickled."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initialize a custom object instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the stored attributes of the object."""
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and write it to a file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as exc:
            print("Error occurred:", exc)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file."""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as exc:
            print("Error occurred:", exc)
            return None
