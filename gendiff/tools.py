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


def formating_value(string, indent):
    string = string.replace('True', 'true')
    string = string.replace('False', 'false')
    string = string.replace('None', 'null')
    return string

def formating_children(d, symb='    ', count=1, depth=1):
    result = []
    indent = symb * count * depth
    for key, value in d.items():
        if isinstance(value, dict):
            result.append(formating_children(value, symb, count, depth+1))
        else:
            result.append(f'\n{{{indent}{key} : {value}')
            result.append(indent+'}')
    return '\n'.join(result)

def formating(data, symb='    ', count=1, depth=1):
    result = []
    indent = symb * count * depth

    for groups, value in data.items():
        if isinstance(value, dict):
            symb_diff = '  '
            result.append(f'{indent}{symb_diff}{groups}: {{')
            result.append(formating(value, symb, count, depth + 1))
            result.append(f'{indent}{symb_diff}}}')
        else:
            if isinstance(value[0], dict):
                value = (formating_children(value[0], symb='    ', count=1, depth=1), *value[1:])

            symb_diff = ' '
            if value[1] == "missing_file_1":
                symb_diff = '+'
            elif value[1] == "missing_file_2":
                symb_diff = '-'
            if "different value" not in value:
                result.append(f'{indent}{symb_diff} {groups}: {value[0]}')
            else:
                result.append(f'{indent}- {groups}: {value[0]}')
                result.append(f'{indent}+ {groups}: {value[1]}')

    return formating_value('\n'.join(result), indent)


def find_differences(file_1, file_2):
    result = {}
    keys = sorted(file_1.keys() | file_2.keys())
    for key in keys:
        value_1, value_2 = file_1.get(key), file_2.get(key)
        if key not in file_1:
            result[key] = (value_2, "missing_file_1")
        elif key not in file_2:
            result[key] = (value_1, "missing_file_2")
        elif value_1 == value_2:
            result[key] = (value_1, 'equal')
        elif isinstance(value_1, dict) and isinstance(value_2, dict):
            result[key] = (find_differences(value_1, value_2))
        else:
            result[key] = (value_1, value_2, "different value")
    print(result)
    return result
