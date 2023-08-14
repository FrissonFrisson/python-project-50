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
    filename_2, file_exе_2 = os.path.splitext(path_2)
    if file_ext_1 == '.json' and file_exе_2 == '.json':
        return json.load(open(path_1)), json.load(open(path_2))
    elif file_ext_1 == '.yaml' or '.yml' and file_exе_2 == '.yaml' or '.yml':
        return yaml.safe_load(open(path_1)), yaml.safe_load(open(path_2))
    elif file_ext_1 == '.yaml' or '.yml' and file_exе_2 == '.json':
        return yaml.safe_load(open(path_1)), json.load(open(path_2))
    elif file_exе_2 == '.yaml' or '.yml' and file_ext_1 == '.json':
        return json.load(open(path_1)), yaml.safe_load(open(path_2))
    else:
        return
