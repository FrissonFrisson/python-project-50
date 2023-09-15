

def format_nested(value, indent, depth=0):
    if not isinstance(value, dict):
        return format_value(str(value))

    def inner(value, depth):
        result = []
        child_indent = indent * depth
        for key, value in value.items():
            if isinstance(value, dict):
                result.append(f'{child_indent}{key}: {{')
                result.append(f'{inner(value, depth + 1)}')
            else:
                result.append(f'{child_indent}{key}: {value}')
        result.append(indent * (depth - 1) + '}')
        return format_value('\n'.join(result))

    return '{' + '\n' + inner(value, depth)


def format_stylish(data):
    def inner(data, symb=' ', count=4, depth=1):
        result = []
        indent = (symb * count * depth)[:-2]
        for diff in data:
            key = diff.get('key')
            value = diff.get('value')
            status = diff.get('status')
            symb_diff = ' '  # default symb if values is equal
            symb_diff = '+' if status == 'added' else symb_diff
            symb_diff = '-' if status == 'removed' else symb_diff
            if status == 'nested':
                result.append(f'{indent}{symb_diff} {key}: {{')
                result.append(inner(diff['nested'], depth = depth + 1))
                result.append(f'{indent}{symb_diff} }}')
            else:
                value = format_nested(value, symb * count, depth + 1)
                if status == 'different':
                    symb_diff = ['-', '+']
                    for value, symb_diff in zip(diff.get('value'), symb_diff):
                        value = format_nested(value, symb * count, depth + 1)
                        result.append(f'{indent}{symb_diff} {key}: {value}')
                else:
                    result.append(f'{indent}{symb_diff} {key}: {value}')
        return '\n'.join(result)
    return '{\n' + inner(data) + '\n}'


def format_value(string):
    string = string.replace('True', 'true')
    string = string.replace('False', 'false')
    string = string.replace('None', 'null')
    return string
    