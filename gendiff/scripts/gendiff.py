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
    set format of output''')
    args = parser.parse_args()
    print(gen_diff(args.first_file, args.second_file))


def gen_diff(path_file_1, path_file_2):
    file_1, file_2 = tools.load_file(path_file_1, path_file_2)
    return tools.formating(tools.parsing(file_1, file_2))


if __name__ == '__main__':
    main()
