import pytest
import os
import json
from things_to_test_hw import add_from_json


@pytest.fixture(autouse=True)
def create_file():
    data = {'a': 3, 'b': 4}
    with open('D:\programs\homework_7\\test', 'w') as file:
        json.dump(data, file)
    yield
    os.remove('D:\programs\homework_7\\test')


@pytest.mark.parametrize(
    'data, expected_result',
    (
            ('a', 3),
            ('b', 4),
            ('ab', 7),
    ),
)
def test_positive(data, expected_result):
    assert add_from_json('D:\programs\homework_7\\test', data) == expected_result


def test_negative_file():
    with pytest.raises(FileNotFoundError) as exc:
        add_from_json('D:\programs\homework_7\\tes', 'lin')
    assert 'No such file or directory' in str(exc.value)


def test_negative_type():
    with pytest.raises(TypeError) as exc:
        add_from_json('D:\programs\homework_7\\test', 35)
    assert "'int' object is not iterable" in str(exc.value)