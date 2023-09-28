import json


def format_recursive(differences, path=''):
    result = []
    for diff in differences:
        key = diff.get('key')
        status = diff.get('status')
        value = format_value(diff.get('value'))
        tree = f"{path}.{key}" if path else key
        if status == 'nested':
            nested_diffs = diff.get('nested')
            result.append(format_recursive(nested_diffs, path=tree))
        elif status == 'added':
            result.append(f"Property '{tree}' was added with value: {value}")
        elif status == 'removed':
            result.append(f"Property '{tree}' was removed")
        elif status == 'changed':
            old = format_value(diff.get('old_value'))
            new = format_value(diff.get('new_value'))
            result.append(f"Property '{tree}' was updated. From {old} to {new}")

    return '\n'.join(result)


def format_plain(differences):
    return format_recursive(differences)


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, bool) or value is None:
        return json.dumps(value)
    return value
