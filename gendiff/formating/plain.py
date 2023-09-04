from gendiff.formating.tools_formating import formating_value


def format_plain(differences, path=''):
    result = []
    for diff in differences:
        key = diff.get('key')
        status = diff.get('status')
        value = format_complex(diff.get('value'))
        tree = f"{path}.{key}" if path else key

        if status == 'nested':
            nested_diffs = diff.get('nested')
            result.append(format_plain(nested_diffs, path=tree))
        elif status == 'missing_file_1':
            result.append(f"Property '{tree}' was added with value: {value}")
        elif status == 'missing_file_2':
            result.append(f"Property '{tree}' was removed")
        elif status == 'different':
            old, new = value
            result.append(f"Property '{tree}' was updated. From {old} to {new}")

    return formating_value('\n'.join(result))


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