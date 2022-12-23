import json


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
            return self._data[table_name]['data']

        raise ValueError('no such a table')

    def add_to_table(self, table_name, item, *items):
        if table_name in self._data:
            items = (item,) + items

            if not all(isinstance(it, self._data[table_name]['structure']) for it in items):
                raise ValueError('invalid data')

            self._data[table_name]['data'].extend(items)

        else:
            raise ValueError('no such a table')


if __name__ == '__main__':
    string = Storage()
    string.add_table('string', str)
    string.add_to_table('string', 's')
    print(string.get_from_table('string'))