#!/usr/bin/env python3
import argparse
from gendiff import tools


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
    file_1, file_2 = tools.parsing(path_file_1, path_file_2)
    diff = tools.find_differences(file_1, file_2)
    if format_name == "plain":
        return tools.format_plain(diff)
    return tools.format_stylish(diff)


if __name__ == '__main__':
    main()
