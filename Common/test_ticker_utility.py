import unittest
import ticker_utility

class TestTickerUtility(unittest.TestCase):

    def test_get_ticker_currency(self):

        self.assertEqual(ticker_utility.get_ticker_currency('D05.SI'), 'SGD')
        self.assertEqual(ticker_utility.get_ticker_currency('2318.HK'), 'HKD')
        self.assertEqual(ticker_utility.get_ticker_currency('510310.SS'), 'CNY')
        self.assertEqual(ticker_utility.get_ticker_currency('AMZN'), 'USD')

if __name__ == '__main__':
    unittest.main()
