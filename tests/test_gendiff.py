from gendiff import generate_diff


def test_generate_diff_format_stylish():
    file_1 = 'tests/fixtures/fixture_1.json'
    file_2 = 'tests/fixtures/fixture_2.json'
    result = open('tests/fixtures/fixture_result_1x2_stylish.txt', "r").read()
    assert generate_diff(file_1, file_2, 'stylish') == result
    file_1 = 'tests/fixtures/fixture_3.yaml'
    file_2 = 'tests/fixtures/fixture_4.yml'
    result = open('tests/fixtures/fixture_result_3x4_stylish.txt', "r").read()
    assert generate_diff(file_1, file_2, 'stylish') == result
    file_1 = 'tests/fixtures/fixture_3.yaml'
    file_2 = 'tests/fixtures/fixture_2.json'
    result = open('tests/fixtures/fixture_result_3x2_stylish.txt', "r").read()
    assert generate_diff(file_1, file_2, 'stylish') == result
    file_1 = 'tests/fixtures/fixture_5.yml'
    file_2 = 'tests/fixtures/fixture_6.yml'
    result = open('tests/fixtures/fixture_result_5x6_stylish.txt', "r").read()
    assert generate_diff(file_1, file_2, 'stylish') == result
    file_1 = 'tests/fixtures/fixture_7.json'
    file_2 = 'tests/fixtures/fixture_8.json'
    result = open('tests/fixtures/fixture_result_7x8_stylish.txt', "r").read()
    assert generate_diff(file_1, file_2, 'stylish') == result


def test_generate_diff_format_plain():
    file_1 = 'tests/fixtures/fixture_1.json'
    file_2 = 'tests/fixtures/fixture_2.json'
    result = open('tests/fixtures/fixture_result_1x2_plain.txt', "r").read()
    assert generate_diff(file_1, file_2, 'plain') == result
    file_1 = 'tests/fixtures/fixture_3.yaml'
    file_2 = 'tests/fixtures/fixture_4.yml'
    result = open('tests/fixtures/fixture_result_3x4_plain.txt', "r").read()
    assert generate_diff(file_1, file_2, 'plain') == result
    file_1 = 'tests/fixtures/fixture_5.yml'
    file_2 = 'tests/fixtures/fixture_6.yml'
    result = open('tests/fixtures/fixture_result_5x6_plain.txt', "r").read()
    assert generate_diff(file_1, file_2, 'plain') == result
    file_1 = 'tests/fixtures/fixture_7.json'
    file_2 = 'tests/fixtures/fixture_8.json'
    result = open('tests/fixtures/fixture_result_7x8_plain.txt', "r").read()
    assert generate_diff(file_1, file_2, 'plain') == result


def test_generate_diff_format_json():
    file_1 = 'tests/fixtures/fixture_1.json'
    file_2 = 'tests/fixtures/fixture_2.json'
    result = open('tests/fixtures/fixture_result_1x2_json.txt', "r").read()
    assert generate_diff(file_1, file_2, 'json') == result
    file_1 = 'tests/fixtures/fixture_3.yaml'
    file_2 = 'tests/fixtures/fixture_4.yml'
    result = open('tests/fixtures/fixture_result_3x4_json.txt', "r").read()
    assert generate_diff(file_1, file_2, 'json') == result
    file_1 = 'tests/fixtures/fixture_5.yml'
    file_2 = 'tests/fixtures/fixture_6.yml'
    result = open('tests/fixtures/fixture_result_5x6_json.txt', "r").read()
    assert generate_diff(file_1, file_2, 'json') == result
    file_1 = 'tests/fixtures/fixture_7.json'
    file_2 = 'tests/fixtures/fixture_8.json'
    result = open('tests/fixtures/fixture_result_7x8_json.txt', "r").read()
    assert generate_diff(file_1, file_2, 'json') == result
