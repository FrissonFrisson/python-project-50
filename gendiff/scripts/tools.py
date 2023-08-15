#!/usr/bin/env python3
import json
import yaml
import os


def formating(result):
    string = '{\n'+'\n'.join(result)+'\n}'
    string = string.replace('True', 'true')
    string = string.replace('False', 'false')
    string = string.replace('None', 'null')
    return string


def load_file(path_1, path_2):
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


def parsing(file_1, file_2):
    keys = sorted(file_1.keys() | file_2.keys())
    result = []
    for key in keys:
        if key not in file_1:
            result.append(f'  + {key}: {file_2[key]}')
        elif key not in file_2:
            result.append(f'  - {key}: {file_1[key]}')
        elif file_1[key] == file_2[key]:
            result.append(f'    {key}: {file_1[key]}')
        elif file_1[key] != file_2[key]:
            result.append(f'  - {key}: {file_1[key]}')
            result.append(f'  + {key}: {file_2[key]}')
    return result
