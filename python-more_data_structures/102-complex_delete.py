#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = []
    for key, valueof in a_dictionary.items():
        if valueof == value:
            key_list.append(key)
    for key in key_list:
        del a_dictionary[key]
    return a_dictionary
