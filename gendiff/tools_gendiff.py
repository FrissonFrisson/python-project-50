import json
import yaml
import os


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
