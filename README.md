


## Hexlet tests and linter status:

[![Actions Status](https://github.com/FrissonFrisson/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/FrissonFrisson/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/678c5be549e7e79148fc/maintainability)](https://codeclimate.com/github/FrissonFrisson/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/678c5be549e7e79148fc/test_coverage)](https://codeclimate.com/github/FrissonFrisson/python-project-50/test_coverage)

[![Frisson Lint](https://github.com/FrissonFrisson/python-project-50/actions/workflows/check_lint.yml/badge.svg)](https://github.com/FrissonFrisson/python-project-50/actions/workflows/check_lint.yml)

```
░██████╗░███████╗███╗░░██╗  ██████╗░██╗███████╗███████╗
██╔════╝░██╔════╝████╗░██║  ██╔══██╗██║██╔════╝██╔════╝
██║░░██╗░█████╗░░██╔██╗██║  ██║░░██║██║█████╗░░█████╗░░
██║░░╚██╗██╔══╝░░██║╚████║  ██║░░██║██║██╔══╝░░██╔══╝░░
╚██████╔╝███████╗██║░╚███║  ██████╔╝██║██║░░░░░██║░░░░░
░╚═════╝░╚══════╝╚═╝░░╚══╝  ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░░░░
```

GEN DIFF is a program that looks for differences between two files (file formats must be json or yaml; you can also compare these formats with each other) with the ability to choose what format the comparison result will be in

# Installation

Clone the repository and install manually:

```bash
$ gh repo clone FrissonFrisson/python-project-50
$ make install
```

# GEN DIFF Launch Instructions


| Format| Command                        | Description                                              |
|------|--------------------------------|--------------------------------------------------------- |
| STYLISH | gendiff path1 path2 or gendiff -f stylish path1 path2 |standard result formatting|
| JSON  | gendiff -f json path1 path2 |result in json format|
| PLAIN | gendiff -f plain path1 path2 |result in plain format|

# Examples of program operation

### Not nested JSON
[![asciicast](https://asciinema.org/a/WeZ6UAxTIVTtu1LPFz5p4dKpv.svg)](https://asciinema.org/a/WeZ6UAxTIVTtu1LPFz5p4dKpv)

### Not nested YAML
[![asciicast](https://asciinema.org/a/dY1gknXdeb5Jqm2cnDqesVSi7.svg)](https://asciinema.org/a/dY1gknXdeb5Jqm2cnDqesVSi7)

### Nested JSON
[![asciicast](https://asciinema.org/a/NMqKBoxZkYSZDm6HV0v4Yi8g1.svg)](https://asciinema.org/a/NMqKBoxZkYSZDm6HV0v4Yi8g1)

### Formatting
[![asciicast](https://asciinema.org/a/89w2yX5CtzOz7mFunfTeNSMq3.svg)](https://asciinema.org/a/89w2yX5CtzOz7mFunfTeNSMq3)
