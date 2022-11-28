import unittest
from os.path import exists
from query import *
from yahoo_fin_ import *

class TestQuery(unittest.TestCase):

    def setUp(self):
        self.yahoo_fin = Yahoo_Fin("amzn", "2009-12-4", data_dir='test_data')
        if not exists(self.yahoo_fin.file_path):
            self.yahoo_fin.get_price()
    
    def test_get_last_price(self):
        query = Query('amzn', 'test_data')
        self.assertGreater(query.get_last_price(), 0)

    def test_get_last_date(self):
        query = Query('amzn', 'test_data')
        self.assertIsNotNone(query.get_last_date())

if __name__ == '__main__':
    unittest.main()
