import pytest

from gendiff import gen_diff


def test_gen_diff():
    file_1 = 'tests/fixtures/fixture_1.json'
    file_2 = 'tests/fixtures/fixture_2.json'
    result = open('tests/fixtures/fixture_result_1x2.txt', "r").read()
    assert gen_diff(file_1, file_2, 'stylish') == result
    file_1 = 'tests/fixtures/fixture_3.yaml'
    file_2 = 'tests/fixtures/fixture_4.yml'
    result = open('tests/fixtures/fixture_result_3x4.txt', "r").read()
    assert gen_diff(file_1, file_2, 'stylish') == result
    file_1 = 'tests/fixtures/fixture_3.yaml'
    file_2 = 'tests/fixtures/fixture_2.json'
    result = open('tests/fixtures/fixture_result_3x2.txt', "r").read()
    assert gen_diff(file_1, file_2, 'stylish') == result
    file_1 = 'tests/fixtures/fixture_5.yml'
    file_2 = 'tests/fixtures/fixture_6.json'
    result = open('tests/fixtures/fixture_result_5x6.txt', "r").read()
    assert gen_diff(file_1, file_2, 'stylish') == result
