import pytest
import os
from things_to_test_hw import search_in_file


@pytest.fixture(autouse=True)
def create_file():
    lines = ['first_line\n', 'second_lin\n', 'third_line\n']
    with open('D:\programs\homework_7\\test', 'w') as file:
        for line in lines:
            file.write(line)
    yield
    os.remove('D:\programs\homework_7\\test')


@pytest.mark.parametrize(
    'search, expected_result',
    (
            ('lin', ['first_line\n', 'second_lin\n', 'third_line\n']),
            ('line', ['first_line\n', 'third_line\n']),
            ('first', ['first_line\n']),
            ('fourth', [])
    ),
)
def test_positive(search, expected_result):
    assert search_in_file('D:\programs\homework_7\\test', search) == expected_result


def test_negative_file():
    with pytest.raises(FileNotFoundError) as exc:
        search_in_file('D:\programs\homework_7\\tes', 'lin')
    assert 'No such file or directory' in str(exc.value)


def test_negative_type():
    with pytest.raises(TypeError) as exc:
        search_in_file('D:\programs\homework_7\\test', 35)
    assert "'in <string>' requires string as left operand, not int" in str(exc.value)
