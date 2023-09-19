import pytest
from gendiff import generate_diff


@pytest.mark.parametrize('file_1, file_2, format, expected_result', [
    ('tests/fixtures/fixture_1.json', 'tests/fixtures/fixture_2.json', 'stylish', 'tests/fixtures/fixture_result_1x2_stylish.txt'),
    ('tests/fixtures/fixture_3.yaml', 'tests/fixtures/fixture_4.yml', 'stylish', 'tests/fixtures/fixture_result_3x4_stylish.txt'),
    ('tests/fixtures/fixture_3.yaml', 'tests/fixtures/fixture_2.json', 'stylish', 'tests/fixtures/fixture_result_3x2_stylish.txt'),
    ('tests/fixtures/fixture_5.yml', 'tests/fixtures/fixture_6.yml', 'stylish', 'tests/fixtures/fixture_result_5x6_stylish.txt'),
    ('tests/fixtures/fixture_7.json', 'tests/fixtures/fixture_8.json', 'stylish', 'tests/fixtures/fixture_result_7x8_stylish.txt'),
    ('tests/fixtures/fixture_1.json', 'tests/fixtures/fixture_2.json', 'plain', 'tests/fixtures/fixture_result_1x2_plain.txt'),
    ('tests/fixtures/fixture_3.yaml', 'tests/fixtures/fixture_4.yml', 'plain', 'tests/fixtures/fixture_result_3x4_plain.txt'),
    ('tests/fixtures/fixture_5.yml', 'tests/fixtures/fixture_6.yml', 'plain', 'tests/fixtures/fixture_result_5x6_plain.txt'),
    ('tests/fixtures/fixture_7.json', 'tests/fixtures/fixture_8.json', 'plain', 'tests/fixtures/fixture_result_7x8_plain.txt'),
    ('tests/fixtures/fixture_1.json', 'tests/fixtures/fixture_2.json', 'json', 'tests/fixtures/fixture_result_1x2_json.txt'),
    ('tests/fixtures/fixture_3.yaml', 'tests/fixtures/fixture_4.yml', 'json', 'tests/fixtures/fixture_result_3x4_json.txt'),
    ('tests/fixtures/fixture_5.yml', 'tests/fixtures/fixture_6.yml', 'json', 'tests/fixtures/fixture_result_5x6_json.txt'),
    ('tests/fixtures/fixture_7.json', 'tests/fixtures/fixture_8.json', 'json', 'tests/fixtures/fixture_result_7x8_json.txt')
])
def test_generate_diff(file_1, file_2, format, expected_result):
    result = open(expected_result, "r").read()
    assert generate_diff(file_1, file_2, format) == result
