import unittest
from dividend import *

class TestDividend(unittest.TestCase):

    def test_get_data(self):
        d = Dividend('test_data')
        data = d.get_data()
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()
