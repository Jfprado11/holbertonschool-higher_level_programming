#!/usr/bin/python3
"""
a script that adds all arguments to a python
list, and then save into a file
"""
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

py_list = []
if os.path.exists("add_item.json"):
    py_list = load_from_json_file("add_item.json")
    for x in range(1, len(sys.argv)):
        py_list.append(sys.argv[x])
    save_to_json_file(py_list, "add_item.json")
else:
    for x in range(1, len(sys.argv)):
        py_list.append(sys.argv[x])
    save_to_json_file(py_list, "add_item.json")
