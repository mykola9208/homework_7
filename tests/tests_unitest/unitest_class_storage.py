import unittest
from things_to_test_hw import Storage

class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        Storage.add_table('string', str)

