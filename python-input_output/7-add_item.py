#!/usr/bin/python3
"""Module for adding command-line arguments to a JSON collection file."""

from importlib.util import module_from_spec, spec_from_file_location
from os import path
from pathlib import Path
from sys import argv

module_dir = Path(__file__).resolve().parent

save_spec = spec_from_file_location(
    'save_to_json_file', module_dir / '5-save_to_json_file.py')
save_module = module_from_spec(save_spec)
save_spec.loader.exec_module(save_module)
save_to_json_file = save_module.save_to_json_file

load_spec = spec_from_file_location(
    'load_from_json_file', module_dir / '6-load_from_json_file.py')
load_module = module_from_spec(load_spec)
load_spec.loader.exec_module(load_module)
load_from_json_file = load_module.load_from_json_file

if path.exists('add_item.json'):
    obj_json_file = load_from_json_file('add_item.json')
else:
    obj_json_file = []

for i in range(1, len(argv)):
    obj_json_file.append(argv[i])

save_to_json_file(obj_json_file, 'add_item.json')
