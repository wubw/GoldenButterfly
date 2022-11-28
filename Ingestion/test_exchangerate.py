import unittest
from exchangerate import *

class TestExchangeRateHost(unittest.TestCase):

    def test_get_exchangerate_raw(self):
        er = ExchangeRateHost()
        ret = er.get_exchangerate_raw('2000-01-01', '2000-01-31', 'NOK,USD,SGD,CNY,HKD')
        self.assertIsNotNone(ret)
        self.assertTrue('2000-01-01' in ret['rates'])
        self.assertTrue('2000-01-31' in ret['rates'])

    def test_get_exchangerate_raw_yearly(self):
        er = ExchangeRateHost()
        ret = er.get_exchangerate_raw_yearly(2001, 'NOK,USD,SGD,CNY,HKD')
        self.assertIsNotNone(ret)
        self.assertTrue('2001-01-01' in ret['rates'])
        self.assertTrue('2001-12-31' in ret['rates'])

    def test_get_exchange_rate(self):
        er = ExchangeRateHost()
        rate = er.get_exchange_rate('USD', 'SGD')
        self.assertGreater(rate, 1)

if __name__ == '__main__':
    unittest.main()
