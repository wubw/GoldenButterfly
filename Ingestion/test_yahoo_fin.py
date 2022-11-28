import unittest
from os.path import exists
from yahoo_fin_ import *

class TestYahooFin(unittest.TestCase):
    
    def setUp(self):
        self.yahoo_fin = Yahoo_Fin("amzn", "2009-12-4", data_dir='test_data')
        if exists(self.yahoo_fin.file_path):
            os.remove(self.yahoo_fin.file_path)

    def test_get_price(self):
        price = self.yahoo_fin.get_price()
        self.assertFalse(price.empty)
        self.assertTrue('ticker' in price)
        self.assertTrue('adjclose' in price)

    def test_save(self):
        self.assertFalse(exists(self.yahoo_fin.file_path))
        self.yahoo_fin.save()
        self.assertTrue(exists(self.yahoo_fin.file_path))
        

if __name__ == '__main__':
    unittest.main()
