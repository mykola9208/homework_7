import json
import os


def search_in_file(file_path, pattern):
    with open(file_path, 'r') as file:
        return [line for line in file if pattern in line]


def add_from_json(file_path, keys_to_use):
    with open(file_path, 'r') as file:
        data = json.load(file)

    return sum(data[key] for key in keys_to_use)


class Storage:
    def __init__(self):
        self._data = {}

    def add_table(self, table_name, structure):
        if table_name in self._data:
            raise ValueError('cannot override table')

        self._data[table_name] = {
            'name': table_name,
            'structure': structure,
            'data': [],
        }

    def get_from_table(self, table_name):
        if table_name in self._data:
            raise ValueError('no such a table')

        return self._data[table_name]['data']

    def add_to_table(self, table_name, item, *items):
        if table_name in self._data:
            raise ValueError('no such a table')

        items = (item,) + items
        if not all(isinstance(it, self._data[table_name]['structure']) for it in items):
            raise ValueError('invalid data')

        self._data[table_name]['data'].extend(items)


if __name__ == '__main__':
    data = {'a': 3, 'b': 4}
    with open('D:\programs\homework_7\\test', 'w') as file:
        json.dump(data, file)
    print(add_from_json('D:\programs\homework_7\\test', 3))
    os.remove('D:\programs\homework_7\\test')
