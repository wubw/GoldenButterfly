import unittest
from stock_ledger import *

class TestStockLedger(unittest.TestCase):

    def test_get_data(self):
        stocker_ledger = StockLedger('test_data')
        data = stocker_ledger.get_data()
        self.assertIsNotNone(data)
        self.assertTrue('ticker' in data)

    def test_get_tickers(self):
        stocker_ledger = StockLedger('test_data')
        tickers = stocker_ledger.get_tickers()
        self.assertIsNotNone(tickers)
        self.assertGreater(len(tickers), 0)

    def test_get_lots(self):
        stocker_ledger = StockLedger('test_data')
        lots = stocker_ledger.get_lots('SPY')
        self.assertIsNotNone(lots)
        self.assertGreater(len(lots), 0)

    def test_get_positions(self):
        stocker_ledger = StockLedger('test_data')
        positions = stocker_ledger.get_positions()
        print(positions)
        self.assertIsNotNone(positions)
        self.assertGreater(len(positions), 0)

        self.assertEquals(positions[positions['ticker']=='D05.SI'].iloc[0]['quantity'], 700)
        self.assertEquals(positions[positions['ticker']=='ME8U.SI'].iloc[0]['quantity'], 7000)
        self.assertEquals(positions[positions['ticker']=='AJBU.SI'].iloc[0]['quantity'], 7200)
        self.assertEquals(positions[positions['ticker']=='C2PU.SI'].iloc[0]['quantity'], 4200)
        self.assertEquals(positions[positions['ticker']=='BABA'].iloc[0]['quantity'], 101)
        self.assertEquals(positions[positions['ticker']=='AAPL'].iloc[0]['quantity'], 115)
        self.assertEquals(positions[positions['ticker']=='MSFT'].iloc[0]['quantity'], 66)
        self.assertEquals(positions[positions['ticker']=='NVDA'].iloc[0]['quantity'], 86)
        self.assertEquals(positions[positions['ticker']=='ARKK'].iloc[0]['quantity'], 176)
        self.assertEquals(positions[positions['ticker']=='SPY'].iloc[0]['quantity'], 45)
        self.assertEquals(positions[positions['ticker']=='ARKW'].iloc[0]['quantity'], 46)
        self.assertEquals(positions[positions['ticker']=='ARKG'].iloc[0]['quantity'], 253)
        self.assertEquals(positions[positions['ticker']=='ARKQ'].iloc[0]['quantity'], 96)
        self.assertEquals(positions[positions['ticker']=='ARKF'].iloc[0]['quantity'], 196)
        self.assertEquals(positions[positions['ticker']=='META'].iloc[0]['quantity'], 89)
        self.assertEquals(positions[positions['ticker']=='PRNT'].iloc[0]['quantity'], 232)
        self.assertEquals(positions[positions['ticker']=='TSLA'].iloc[0]['quantity'], 90)
        self.assertEquals(positions[positions['ticker']=='SOXX'].iloc[0]['quantity'], 93)
        self.assertEquals(positions[positions['ticker']=='U'].iloc[0]['quantity'], 136)
        self.assertEquals(positions[positions['ticker']=='QQQ'].iloc[0]['quantity'], 47)
        self.assertEquals(positions[positions['ticker']=='CQQQ'].iloc[0]['quantity'], 190)
        self.assertEquals(positions[positions['ticker']=='0700.HK'].iloc[0]['quantity'], 600)
        self.assertEquals(positions[positions['ticker']=='2318.HK'].iloc[0]['quantity'], 3000)
        self.assertEquals(positions[positions['ticker']=='J69U.SI'].iloc[0]['quantity'], 4600)
        self.assertEquals(positions[positions['ticker']=='1299.HK'].iloc[0]['quantity'], 800)
        self.assertEquals(positions[positions['ticker']=='1398.HK'].iloc[0]['quantity'], 19000)
        self.assertEquals(positions[positions['ticker']=='M44U.SI'].iloc[0]['quantity'], 9000)
        self.assertEquals(positions[positions['ticker']=='GOOG'].iloc[0]['quantity'], 220)
        self.assertEquals(positions[positions['ticker']=='3988.HK'].iloc[0]['quantity'], 11000)
        self.assertEquals(positions[positions['ticker']=='C38U.SI'].iloc[0]['quantity'], 6000)
        self.assertEquals(positions[positions['ticker']=='PYPL'].iloc[0]['quantity'], 104)
        self.assertEquals(positions[positions['ticker']=='EDU'].iloc[0]['quantity'], 50)
        self.assertEquals(positions[positions['ticker']=='9988.HK'].iloc[0]['quantity'], 1400)
        self.assertEquals(positions[positions['ticker']=='XLV'].iloc[0]['quantity'], 25)
        self.assertEquals(positions[positions['ticker']=='AMZN'].iloc[0]['quantity'], 81)
        self.assertEquals(positions[positions['ticker']=='9618.HK'].iloc[0]['quantity'], 19)
        self.assertEquals(positions[positions['ticker']=='510310.SS'].iloc[0]['quantity'], 182800)

        self.assertAlmostEqual(positions[positions['ticker']=='510310.SS'].iloc[0]['cost'], 346517.1, 2)
        self.assertAlmostEqual(positions[positions['ticker']=='SOXX'].iloc[0]['cost'], 39249.698372, 2)

        self.assertAlmostEqual(positions[positions['ticker']=='510310.SS'].iloc[0]['avg price'], 1.895608, 2)
        self.assertAlmostEqual(positions[positions['ticker']=='SOXX'].iloc[0]['avg price'], 422.039767, 2)

if __name__ == '__main__':
    unittest.main()
