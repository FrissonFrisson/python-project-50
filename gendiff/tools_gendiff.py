import json
import yaml
import os
from gendiff.formating.stylish import format_stylish
from gendiff.formating.plain import format_plain
from gendiff.formating.json import format_json


def choose_format(format_name, diff):
    if format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    return format_stylish(diff)


def pars(path):
    filename, file_ext = os.path.splitext(path)
    file = {}
    if file_ext == '.json':
        file = json.load(open(path))
    elif file_ext in ['.yaml', '.yml']:
        file = yaml.safe_load(open(path))
    return file


def find_differences(file, file_2):
    changed = []
    keys = sorted(file.keys() | file_2.keys())
    for key in keys:
        result = {'key': key}
        value_1, value_2 = file.get(key), file_2.get(key)
        if key not in file:
            result['value'] = value_2
            result['status'] = 'added'
        elif key not in file_2:
            result['value'] = value_1
            result['status'] = 'removed'
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


def generate_diff(path_file_1, path_file_2, format_name='stylish'):
    file_1, file_2 = pars(path_file_1), pars(path_file_2)
    diff = find_differences(file_1, file_2)
    return choose_format(format_name, diff)
