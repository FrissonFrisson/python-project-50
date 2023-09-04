#!/usr/bin/env python3
import argparse
from gendiff.tools_gendiff import find_differences, parsing
from gendiff.formating.stylish import format_stylish
from gendiff.formating.plain import format_plain
import json


def main():
    parser = argparse.ArgumentParser(description='''
    Compares two configuration files and shows a difference.''')
    parser.add_argument('first_file', type=str, help='''
    Path to the first file''')
    parser.add_argument('second_file', type=str, help='''
    Path to the second file''')
    parser.add_argument("-f", "--format", type=str, help='''
    set format of output: stylish. plain or json''')
    args = parser.parse_args()
    print(gen_diff(args.first_file, args.second_file, args.format))


def gen_diff(path_file_1, path_file_2, format_name):
    file_1, file_2 = parsing(path_file_1, path_file_2)
    diff = find_differences(file_1, file_2)
    if format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return json.dumps(diff)
    return format_stylish(diff)


if __name__ == '__main__':
    main()
