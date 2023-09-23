#!/usr/bin/env python3
from gendiff.tools_gendiff import generate_diff, parse_args


def main():
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
