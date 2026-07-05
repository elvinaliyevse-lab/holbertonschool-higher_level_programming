#!/usr/bin/python3
"""Basic JSON serialization and deserialization helpers."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON and save it to the specified file."""
    content = json.dumps(data)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def load_and_deserialize(filename):
    """Load a JSON file and return the deserialized object."""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    return json.loads(content)
