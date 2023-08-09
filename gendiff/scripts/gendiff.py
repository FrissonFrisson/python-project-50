#!/usr/bin/env python3
import argparse
import json

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='Path to the first file')
    parser.add_argument('second_file', type=str, help='Path to the second file')
    parser.add_argument("-f", "--format", type=str, help='set format of output')
    args = parser.parse_args()
    print(gen_diff(args.first_file, args.second_file))


def gen_diff(dict_1, dict_2):
    dict_1 = json.load(open(str(dict_1)))
    dict_2 = json.load(open(str(dict_2)))
    keys = sorted(dict_1.keys() | dict_2.keys())
    result = '{\n'
    for key in keys:
        if key not in dict_1:
            result += f'+ {key}: {str(dict_2[key])}\n'
        elif key not in dict_2:
            result += f'- {key}: {str(dict_1[key])}\n'
        elif dict_1[key] == dict_2[key]:
            result += f'  {key}: {str(dict_1[key])}\n'
        elif dict_1[key] != dict_2[key]:
            result += f'- {key}: {str(dict_1[key])}\n+ {key}: {str(dict_2[key])}\n'
    result += '}'
    return result


if __name__ == '__main__':
    main()