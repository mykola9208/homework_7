import pytest
from things_to_test_hw import Storage
string = Storage()
string.add_table('string', str)


def test_positive():
    assert string.get_from_table('string') == []
    string.add_to_table('string', 'a', 'b', 'c')
    assert string.get_from_table('string') == ['a', 'b', 'c']


def test_negative():
    with pytest.raises(ValueError) as exc:
        string.add_table('string', str)
    assert 'cannot override table' in str(exc.value)

    with pytest.raises(ValueError) as exc:
        string.add_to_table('integer', 5)
    assert 'no such a table' in str(exc.value)

    with pytest.raises(ValueError) as exc:
        string.get_from_table('integer')
    assert 'no such a table' in str(exc.value)

    with pytest.raises(ValueError) as exc:
        string.add_to_table('string', 5)
    assert 'invalid data' in str(exc.value)
