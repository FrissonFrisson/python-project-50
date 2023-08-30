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


def formating_value(string):
    string = string.replace('True', 'true')
    string = string.replace('False', 'false')
    string = string.replace('None', 'null')
    return string


def formating_child(child, cur_indent='', cur_depth = 0, symb='    ', count=1):
    def inner(child, depth=1):
        result = []
        depth += count
        indent = (symb * depth)+cur_indent
        for key, value in child.items():
            if isinstance(value, dict):
                result.append(indent + key + ': {')
                result.append(inner(value, depth+1))
                result.append(indent + '}')
            else:
                result.append(f'{indent}{key}: {value}')
        return '\n'.join(result)
    return '{\n'+inner(child,count)+'\n' + cur_indent + '}'


def formating(data, symb='  ', count=1):
    def inner(data, depth=0):
        result = []
        depth += count
        indent = symb * depth
        for groups, value in data.items():
            symb_diff = '  '
            if 'equal keys' in value:
                result.append(f'{indent}{symb_diff}{groups}: {{')
                result.append(inner(value[0], depth + 1))
                result.append(indent+symb_diff+'}')    
            else:
                if isinstance(value[0], dict):
                    cur_indent = indent+symb_diff
                    args_for_formating = (cur_indent, depth, symb, count)
                    child = formating_child(value[0], *args_for_formating)
                    value = (child, *value[1:])
                if "different value" in value:
                    result.append(f'{indent}- {groups}: {value[0]}')
                    result.append(f'{indent}+ {groups}: {value[1]}')
                else:
                    symb_diff = '  ' if "equal" in value else symb_diff
                    symb_diff = '+ ' if "missing_file_1" in value else symb_diff
                    symb_diff = '- ' if "missing_file_2" in value else symb_diff
                    result.append(f'{indent}{symb_diff}{groups}: {value[0]}')
        return '\n'.join(result)
    return formating_value('{\n'+inner(data)+'\n}')


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
            result[key] = (find_differences(value_1, value_2), "equal keys")
        else:
            result[key] = (value_1, value_2, "different value")
    return result
