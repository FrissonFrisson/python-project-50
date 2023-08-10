import pytest
import json
from gendiff import gen_diff

file_1 = 'tests/fixtures/fixture_1.json'
file_2 = 'tests/fixtures/fixture_2.json'
result = open('tests/fixtures/fixture_result_1_2.txt', "r").read()

def test_gen_diff():
    assert gen_diff(file_1, file_2) == result