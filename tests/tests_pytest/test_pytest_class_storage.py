import pytest
from things_to_test_hw import Storage
string = Storage()
string.add_table('string', str)
integer = Storage()
integer.add_table('integer', int)


def test_positive():
    assert string.get_from_table('string') == []
    assert integer.get_from_table('integer') == []
    string.add_to_table('string', 'a', 'b', 'c')
    integer.add_to_table('integer', 5, 6, 78)
    assert string.get_from_table('string') == ['a', 'b', 'c']
    assert integer.get_from_table('integer') == [5, 6, 78]


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

    with pytest.raises(ValueError) as exc:
        integer.add_to_table('integer', 5.5)
    assert 'invalid data' in str(exc.value)
