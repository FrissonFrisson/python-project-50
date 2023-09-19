#!/usr/bin/env python3
import argparse
from gendiff.tools_gendiff import find_differences, pars, choose_format


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
    print(generate_diff(args.first_file, args.second_file, args.format))


def generate_diff(path_file_1, path_file_2, format_name='stylish'):
    file_1, file_2 = pars(path_file_1), pars(path_file_2)
    diff = find_differences(file_1, file_2)
    return choose_format(format_name, diff)


if __name__ == '__main__':
    main()
