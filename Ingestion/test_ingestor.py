import unittest
from os.path import exists
from ingestor import *

class TestIngestor(unittest.TestCase):

    def setUp(self):
        self.yahoo_fin = Yahoo_Fin("amzn", "2009-12-4", end_date="2022-11-08" ,data_dir='test_data')
        if exists(self.yahoo_fin.file_path):
            os.remove(self.yahoo_fin.file_path)
        self.file_path = self.yahoo_fin.file_path
        self.yahoo_fin.save()

    def test_update_data(self):
        l1 = 0
        with open(self.file_path, 'r') as fp:
            l1 = len(fp.readlines())
        
        ingestor = Ingestor('amzn', data_dir='test_data')
        ingestor.update_data()

        l2 = 0
        with open(self.file_path, 'r') as fp:
            l2 = len(fp.readlines())

        self.assertGreater(l2, l1)

if __name__ == '__main__':
    unittest.main()
