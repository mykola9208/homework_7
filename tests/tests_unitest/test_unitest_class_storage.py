import unittest
from things_to_test_hw import Storage
string = Storage()
string.add_table('string', str)
integer = Storage()
integer.add_table('integer', int)


class TestClass(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(string.get_from_table('string'), [])
        self.assertEqual(integer.get_from_table('integer'), [])
        string.add_to_table('string', 'a', 'b', 'c')
        integer.add_to_table('integer', 5, 6, 78)
        self.assertEqual(string.get_from_table('string'), ['a', 'b', 'c'])
        self.assertEqual(integer.get_from_table('integer'), [5, 6, 78])

    def test_negative(self):
        with self.assertRaises(ValueError) as exc:
            string.add_table('string', str)
        self.assertEqual(exc.exception.args, ('cannot override table',))

        with self.assertRaises(ValueError) as exc:
            string.add_to_table('integer', 5)
        self.assertEqual(exc.exception.args, ('no such a table',))

        with self.assertRaises(ValueError) as exc:
            string.get_from_table('integer')
        self.assertEqual(exc.exception.args, ('no such a table',))

        with self.assertRaises(ValueError) as exc:
            string.add_to_table('string', 5)
        self.assertEqual(exc.exception.args, ('invalid data',))

        with self.assertRaises(ValueError) as exc:
            integer.add_to_table('integer', 5.5)
        self.assertEqual(exc.exception.args, ('invalid data',))
