#!/usr/bin/env python3
import json
import yaml
import os


def stringify(data, symb=' ', count=1,):
    def iter_(curent_value, depth=1):
        if not isinstance(curent_value, (list, tuple, set, dict)):
            return str(curent_value)
        result = []
        case_symb = symb*depth*count
        if isinstance(curent_value, (dict)):
            result.append('{')
            for key, value in curent_value.items():
                result.append(f'{case_symb}{key}: {iter_(curent_value[key], depth + 1)}')
        result.append(symb*(depth-1)*count+'}')
        return '\n'.join(result)
    return iter_(data, depth=1)
def formating_value(string):
    string = str(string)
    string = '{\n'+'\n'.join(result)+'\n}'
    string = string.replace('True', 'true')
    string = string.replace('False', 'false')
    string = string.replace('None', 'null')
    return string


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
    

def formating(result, symb=' ', count=1):
    def inner(curent_value, depth=0):
        result = []
        case_symb = symb*depth*count
        for key, value in curent_value.items():
            if "missing_file_1" in value:
                result.append(f'{case_symb}+ {key}: {value[0]}')
            elif "missing_file_2" in value:
                result.append(f'{case_symb}- {key}: {value[0]}')
            elif "equal" in value:
                result.append(f'{case_symb}  {key}: {value[0]}')
            elif "different value" in value:
                result.append(f'{case_symb}- {key}: {value[0]}')
                result.append(f'{case_symb}+ {key}: {value[1]}')
            elif isinstance(value, dict):
                nested_diff = case_symb + inner(value, depth + 1)+'\n' + case_symb + '}'
                result.append(f'{case_symb}{key}: {{')
                result.append(nested_diff)

def format_data(data):
    result = "{\n"
    indent = "  "

    def format_value(value):
        if isinstance(value, dict):
            return format_dict(value)
        elif isinstance(value, tuple):
            if len(value) == 2:
                return f"{value[0]}: {value[1]}"
            elif len(value) == 3:
                return f"{value[0]}: {value[1]} ({value[2]})"
        else:
            return str(value)

    def format_dict(dictionary):
        inner_result = ""
        for key, value in dictionary.items():
            if isinstance(value, dict):
                inner_result += f"{indent}{key}: {format_dict(value)}{indent}{indent}}}\n"
            else:
                inner_result += f"{indent}{key}: {format_value(value)}\n"
        return inner_result

    for key, value in data.items():
        result += f"{indent}{key}: {format_dict(value)}{indent}}}\n"

    result += "}"
    return result

        return '\n'.join(result)
    return inner(result)
                



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
        else:
            if isinstance(value_1, dict) and isinstance(value_2, dict):
                result[key] = (find_differences(value_1, value_2))
            else:
                result[key] = (value_1, value_2, "different value")
    return result