import json


def format_value(value, indent, depth=0):
    if not isinstance(value, dict):
        return format(value)
    result = []
    result.append('{')
    child_indent = indent * depth
    for key, value in value.items():
        value = format_value(value, indent, depth+1)
        result.append(f'{child_indent}{key}: {value}')
    result.append(indent * (depth - 1) + '}')
    return '\n'.join(result)


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


def format(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    return value
