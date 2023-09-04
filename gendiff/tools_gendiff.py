#!/usr/bin/env python3
import json
import yaml
import os


def parsing(path_1, path_2):
    filename_1, file_ext_1 = os.path.splitext(path_1)
    filename_2, file_ext_2 = os.path.splitext(path_2)
    file_1 = {}
    file_2 = {}
    if file_ext_1 == '.json':
        file_1 = json.load(open(path_1))
    elif file_ext_1 in ['.yaml', '.yml']:
        file_1 = yaml.safe_load(open(path_1))
    if file_ext_2 == '.json':
        file_2 = json.load(open(path_2))
    elif file_ext_2 in ['.yaml', '.yml']:
        file_2 = yaml.safe_load(open(path_2))
    return file_1, file_2


def find_differences(file_1, file_2):
    changed = []
    keys = sorted(file_1.keys() | file_2.keys())
    for key in keys:
        result = {'key': key}
        value_1, value_2 = file_1.get(key), file_2.get(key)
        if key not in file_1:
            result['value'] = value_2
            result['status'] = 'missing_file_1'
        elif key not in file_2:
            result['value'] = value_1
            result['status'] = 'missing_file_2'
        elif value_1 == value_2:
            result['value'] = value_1
            result['status'] = 'equal'
        elif isinstance(value_1, dict) and isinstance(value_2, dict):
            result['nested'] = find_differences(value_1, value_2)
            result['status'] = 'nested'
        else:
            result['value'] = [value_1, value_2]
            result['status'] = 'different'
        changed.append(result)
    return changed
