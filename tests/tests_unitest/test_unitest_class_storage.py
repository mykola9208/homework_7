import unittest
from things_to_test_hw import Storage
string = Storage()
string.add_table('string', str)


class TestClass(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(string.get_from_table('string'), [])
        string.add_to_table('string', 'a', 'b', 'c')
        self.assertEqual(string.get_from_table('string'), ['a', 'b', 'c'])

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
