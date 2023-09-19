#!/usr/bin/env python3
import argparse
from gendiff.tools_gendiff import generate_diff


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


if __name__ == '__main__':
    main()
