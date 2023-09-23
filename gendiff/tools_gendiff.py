import json
import yaml
import os
import argparse
from gendiff.formating.stylish import format_stylish
from gendiff.formating.plain import format_plain
from gendiff.formating.json import format_json


def parse_args():
    parser = argparse.ArgumentParser(description='''
    Compares two configuration files and shows a difference.''')
    parser.add_argument('first_file', type=str, help='''
    Path to the first file''')
    parser.add_argument('second_file', type=str, help='''
    Path to the second file''')
    parser.add_argument("-f", "--format", type=str, help='''
    set format of output: stylish. plain or json''')
    args = parser.parse_args()
    return args


def choose_format(format_name, diff):
    if format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    elif format_name == 'stylish' or format_name is None:
        return format_stylish(diff)


def read_file(path):
    with open(path) as file:
        content = file.read()
    return content


def parse_file(path):
    filename, file_ext = os.path.splitext(path)
    file = {}
    if file_ext == '.json':
        file = json.loads(read_file(path))
    elif file_ext in ['.yaml', '.yml']:
        file = yaml.safe_load(read_file(path))
    return file


def find_differences(file_1, file_2):
    changed = []
    keys = sorted(file_1.keys() | file_2.keys())
    for key in keys:
        result = {'key': key}
        value_1, value_2 = file_1.get(key), file_2.get(key)
        if key not in file_1:
            result['value'] = value_2
            result['status'] = 'added'
        elif key not in file_2:
            result['value'] = value_1
            result['status'] = 'removed'
        elif value_1 == value_2:
            result['value'] = value_1
            result['status'] = 'unchanged'
        elif isinstance(value_1, dict) and isinstance(value_2, dict):
            result['nested'] = find_differences(value_1, value_2)
            result['status'] = 'nested'
        else:
            result['old_value'] = value_1
            result['new_value'] = value_2
            result['status'] = 'changed'
        changed.append(result)
    return changed


def generate_diff(path_file_1, path_file_2, format_name='stylish'):
    file_1, file_2 = parse_file(path_file_1), parse_file(path_file_2)
    diff = find_differences(file_1, file_2)
    return choose_format(format_name, diff)
