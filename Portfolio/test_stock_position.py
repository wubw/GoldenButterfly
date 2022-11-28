import unittest
from stock_position import *

class TestStockPosition(unittest.TestCase):

    def test_get_positions(self):
        sp = StockPosition()
        positions = sp.get_positions()
        self.assertIsNotNone(positions)

if __name__ == '__main__':
    unittest.main()
