import unittest
import os
from things_to_test_hw import search_in_file


class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        lines = ['first_line\n', 'second_lin\n', 'third_line\n']
        with open('D:\programs\homework_7\\test', 'w') as file:
            for line in lines:
                file.write(line)

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove('D:\programs\homework_7\\test')

    def test_positive(self):
        self.assertEqual(search_in_file('D:\programs\homework_7\\test', 'lin'), ['first_line\n', 'second_lin\n', 'third_line\n'])
        self.assertEqual(search_in_file('D:\programs\homework_7\\test', 'line'), ['first_line\n', 'third_line\n'])
        self.assertEqual(search_in_file('D:\programs\homework_7\\test', 'first'), ['first_line\n'])
        self.assertEqual(search_in_file('D:\programs\homework_7\\test', 'fourth'), [])

    def test_negaive(self):
        with self.assertRaises(FileNotFoundError) as exc:
            search_in_file('D:\programs\homework_7\\tes', 'lin')

        self.assertEqual(exc.exception.args, (2, 'No such file or directory'))
        with self.assertRaises(TypeError) as exc:
            search_in_file('D:\programs\homework_7\\test', 35)
        self.assertEqual(exc.exception.args, ("'in <string>' requires string as left operand, not int",))