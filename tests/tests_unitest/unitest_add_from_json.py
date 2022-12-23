import unittest
import os
import json
from things_to_test_hw import add_from_json


class TestJson(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        data = {'a': 3, 'b': 4}
        with open('D:\programs\homework_7\\test', 'w') as file:
            json.dump(data, file)

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove('D:\programs\homework_7\\test')

    def test_positive(self):
        self.assertEqual(add_from_json('D:\programs\homework_7\\test', 'a'), 3)
        self.assertEqual(add_from_json('D:\programs\homework_7\\test', 'b'), 4)
        self.assertEqual(add_from_json('D:\programs\homework_7\\test', 'ab'), 7)

    def test_negative(self):
        with self.assertRaises(FileNotFoundError) as exc:
            add_from_json('D:\programs\homework_7\\tes', 'lin')
        self.assertEqual(exc.exception.args, (2, 'No such file or directory'))

        with self.assertRaises(TypeError) as exc:
            add_from_json('D:\programs\homework_7\\test', 35)
        self.assertEqual(exc.exception.args, ("'int' object is not iterable",))

        with self.assertRaises(KeyError) as exc:
            add_from_json('D:\programs\homework_7\\test', 'abc')
        self.assertEqual(exc.exception.args, ('c',))
