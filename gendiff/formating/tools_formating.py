def formating_value(string):
    string = string.replace('True', 'true')
    string = string.replace('False', 'false')
    string = string.replace('None', 'null')
    return string
