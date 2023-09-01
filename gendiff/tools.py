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


def formating_groups(string):
    string = string.replace('True', 'true')
    string = string.replace('False', 'false')
    string = string.replace('None', 'null')
    return string


def formating_no_child(no_child, cur_indent='', symb='    ', count=1):
    def inner(no_child, depth=1):
        result = []
        depth += count
        indent = (symb * depth)+cur_indent
        for key, value in no_child.items():
            if isinstance(value, dict):
                result.append(f'{indent}{key}: {{')
                result.append(inner(value, depth+1)) #go to next level tree
                result.append(indent + '}')
            else:
                result.append(f'{indent}{key}: {value}')
        return '\n'.join(result)
    return '{\n'+inner(no_child, count)+'\n' + cur_indent + '}' #Final format


def format_stylish(data, symb='  ', count=1):
    def inner(data, depth=0):
        result = []
        depth += count
        indent = symb * depth
        for key, groups in data.items():
            symb_diff = ' ' #Default diff symbol if groupss is equal
            if 'children' in groups:
                result.append(f'{indent}{symb_diff} {key}: {{') 
                result.append(inner(groups[0], depth + 1)) #go to next level tree
                result.append(f'{indent}{symb_diff} }}')
            else:
                if isinstance(groups[0], dict): #it`s not children
                    cur_indent = indent+symb_diff+" "
                    args_for_formating = (cur_indent, symb, count)
                    no_child = formating_no_child(groups[0], *args_for_formating)
                    groups = (no_child, *groups[1:])
                if 'different values' in groups:
                    result.append(f'{indent}- {key}: {groups[0]}')
                    result.append(f'{indent}+ {key}: {groups[1]}')
                else:
                    symb_diff = ' ' if 'equal' in groups else symb_diff
                    symb_diff = '+' if 'missing_file_1' in groups else symb_diff
                    symb_diff = '-' if 'missing_file_2' in groups else symb_diff
                    result.append(f'{indent}{symb_diff} {key}: {groups[0]}')
        return '\n'.join(result)
    return formating_groups('{\n'+inner(data)+'\n}')


def format_plain(data):
    def inner(data, key_tree=''):
        diff_property = ''
        result = []
        for key, groups in data.items():
            key_tree += key
            if 'children' in groups:
                result.append(f'{inner(groups[0], key_tree)}') #go to next level tree
            else:
                if isinstance(groups[0], dict): #it`s not children
                    groups = ('[complex value]', *groups[1:])
                if 'equal' not in groups:
                    diff_property = f'{key_tree} was updated. From {groups[0]} to {groups[1]}' if 'different values' in groups else diff_property
                    diff_property = f'{key_tree} was added with value: {groups[0]}' if 'missing_file_1' in groups else diff_property
                    diff_property = f'{key_tree} was removed' if 'missing_file_2' in groups else diff_property
                    result.append(diff_property)
        return '\n'.join(result)
    return inner(data)


def find_differences(file_1, file_2):
    result = {}
    keys = sorted(file_1.keys() | file_2.keys())
    for key in keys:
        value_1, value_2 = file_1.get(key), file_2.get(key) 
        if key not in file_1:
            result[key] = (value_2, 'missing_file_1') #value missing file_1
        elif key not in file_2:
            result[key] = (value_1, 'missing_file_2') #value missing file_2
        elif value_1 == value_2:
            result[key] = (value_1, 'equal') #values file_1, file_2 is equal 
        elif isinstance(value_1, dict) and isinstance(value_2, dict):
            result[key] = (find_differences(value_1, value_2), 'children') #next level tree
        else:
            result[key] = (value_1, value_2, 'different values') #valuess file_1, file_2 is not equal 
    return result
