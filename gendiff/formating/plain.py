
def format_recursive(differences, path=''):
    result = []
    for diff in differences:
        key = diff.get('key')
        status = diff.get('status')
        value = format_complex(diff.get('value'))
        tree = f"{path}.{key}" if path else key

        if status == 'nested':
            nested_diffs = diff.get('nested')
            result.append(format_recursive(nested_diffs, path=tree))
        elif status == 'added':
            result.append(f"Property '{tree}' was added with value: {value}")
        elif status == 'removed':
            result.append(f"Property '{tree}' was removed")
        elif status == 'different':
            old, new = value
            result.append(f"Property '{tree}' was updated. From {old} to {new}")

    return format_value('\n'.join(result))`


def format_plain(differences):
    return format_recursive(differences)



def format_complex(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, list):
        format_value = []
        for v in value:
            format_value.append(format_complex(v))
        return format_value
    else:
        return str(value)


def format_value(string):
    string = string.replace('True', 'true')
    string = string.replace('False', 'false')
    string = string.replace('None', 'null')
    return string
