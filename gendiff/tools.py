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
    def inner(curent_value, depth=1):
        result = []
        case_symb = symb*depth*count
        for key, value in curent_value.items():
            if value == "missing_file_1":
                result.append(case_symb + '+ ' + key)
            elif value == "missing_file_2":
                result.append(case_symb + '- ' + key)
            elif value == "equal":
                result.append(case_symb + key)
            elif isinstance(value, dict) and not "equal" in key:
                    result.append(case_symb + inner(value, depth + 1))
            elif "equal" in key:
                result.append(case_symb + key[0] + " {")
                if isinstance(value, dict):
                    result.append(case_symb + inner(value, depth + 1))
                elif isinstance(value, tuple):
                    value_1, value_2 = value
                    result.append(case_symb + '- ' + value_1)
                    result.append(case_symb + '+ ' + value_1)
                result.append(case_symb+'}')
            elif isinstance(key, tuple) and value == "different value":
                    value_1, value_2 = key
                    result.append(case_symb + '- ' + value_1)
                    result.append(case_symb + '+ ' + value_1)
                
        return '\n'.join(result)
    return inner(result)
                



def find_differences(file_1, file_2):
    def inner(data_1, data_2):
        result = {}
        keys = sorted(data_1.keys() | data_2.keys())
        for key in keys:
            value_1, value_2 = data_1.get(key), data_2.get(key)
            string_1, string_2 = f'{key}: {value_1}', f'{key}: {value_2}'
            if key not in data_1:
                
                result[string_2] = "missing_file_1"
            elif key not in data_2:
                result[string_1] = "missing_file_2"
            elif value_1 == value_2:
                result[(string_1)] = "equal"
            else:
                if isinstance(value_1, dict) and isinstance(value_2, dict):
                    result[key+':', "equal"] = inner(value_1, value_2)
                else:
                    result[(string_1, string_2)] = "different value"
        return result
    return formating(inner(file_1, file_2))
