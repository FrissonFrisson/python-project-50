

def format_value(value, indent, depth=0):
    if not isinstance(value, dict):
        return format(str(value))

    def inner(value, depth):
        result = []
        child_indent = indent * depth
        for key, value in value.items():
            if isinstance(value, dict):
                result.append(f'{child_indent}{key}: {{')
                result.append(f'{inner(value, depth + 1)}')
            else:
                result.append(f'{child_indent}{key}: {format(str(value))}')
        result.append(indent * (depth - 1) + '}')
        return '\n'.join(result)

    return '{' + '\n' + inner(value, depth)


def format_recursive(data, symb=' ', count=4, depth=1):
    result = []
    diff_indent = (symb * count * depth)[:-2]
    indent = symb * count
    special_symb = ' '
    for diff in data:
        key = diff.get('key')
        status = diff.get('status')
        if status == 'nested':
            result.append(f'{diff_indent}{special_symb} {key}: {{')
            result.append(format_recursive(diff['nested'], depth=depth + 1))
            result.append(f'{diff_indent}{special_symb} }}')
        elif status == 'changed':
            old_value = format_value(diff['old_value'], indent, depth + 1)
            new_value = format_value(diff['new_value'], indent, depth + 1)
            result.append(f'{diff_indent}- {key}: {old_value}')
            result.append(f'{diff_indent}+ {key}: {new_value}')
        else:
            value = format_value(diff['value'], indent, depth + 1)
            symb_diff = {
                'unchanged': ' ',
                'added': '+',
                'removed': '-'
            }
            result.append(f'{diff_indent}{symb_diff[status]} {key}: {value}')
    return '\n'.join(result)


def format_stylish(data):
    return '{\n' + format_recursive(data) + '\n}'


def format(string):
    string = string.replace('True', 'true')
    string = string.replace('False', 'false')
    string = string.replace('None', 'null')
    return string
