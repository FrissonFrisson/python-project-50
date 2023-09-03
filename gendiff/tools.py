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


def formating_to_json(string):
    string = string.replace('True', 'true')
    string = string.replace('False', 'false')
    string = string.replace('None', 'null')
    return string


def formating_value(value, indent, depth=0):
    if not isinstance(value, dict):
        return formating_to_json(str(value))

    def inner(value, depth):
        result = []
        child_indent = indent*depth
        for key, value in value.items():
            if isinstance(value, dict):
                result.append(f'{child_indent}{key}: {{')
                result.append(f'{inner(value, depth + 1)}')
            else:
                result.append(f'{child_indent}{key}: {value}')
        result.append(indent*(depth-1)+'}')
        return formating_to_json('\n'.join(result))

    return '{'+'\n'+inner(value, depth)


def format_stylish(data, symb=' ', count=4):
    def inner(data, depth=1):
        result = []
        indent = (symb * count * depth)[:-2]
        for diff in data:
            key = diff.get('key')
            value = diff.get('value')
            status = diff.get('status')
            symb_diff = ' '  # default symb if values is equal
            symb_diff = '+' if status == 'missing_file_1' else symb_diff
            symb_diff = '-' if status == 'missing_file_2' else symb_diff
            if status == 'nested':
                result.append(f'{indent}{symb_diff} {key}: {{')
                result.append(inner(diff['nested'], depth + 1))
                result.append(f'{indent}{symb_diff} }}')
            else:
                value = formating_value(value, symb*count, depth+1)
                if status == 'different':
                    symb_diff = ['-', '+']
                    for value, symb_diff in zip(diff.get('value'), symb_diff):
                        value = formating_value(value, symb*count, depth+1)
                        result.append(f'{indent}{symb_diff} {key}: {value}')
                else:
                    result.append(f'{indent}{symb_diff} {key}: {value}')
        return '\n'.join(result)
    return '{\n'+inner(data)+'\n}'


def find_differences(file_1, file_2):
    changed = []
    keys = sorted(file_1.keys() | file_2.keys())
    for key in keys:
        result = {'key': key}
        value_1, value_2 = file_1.get(key), file_2.get(key)
        if key not in file_1:
            result['status'] = 'missing_file_1'
            result['value'] = value_2
        elif key not in file_2:
            result['status'] = 'missing_file_2'
            result['value'] = value_1
        elif value_1 == value_2:
            result['status'] = 'equal'
            result['value'] = value_1
        elif isinstance(value_1, dict) and isinstance(value_2, dict):
            result['status'] = 'nested'
            result['nested'] = find_differences(value_1, value_2)
        else:
            result['status'] = 'different'
            result['value'] = [value_1, value_2]
        changed.append(result)
    return changed
