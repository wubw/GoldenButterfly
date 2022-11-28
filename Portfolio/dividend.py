import os
import pandas as pd

import sys
sys.path.insert(1, '../Common')
import ticker_utility

class Dividend:

    def __init__(self, data_dir = 'data'):
        self.file_path_raw = os.path.join(data_dir, 'dividend_raw.csv')
        self.file_path = os.path.join(data_dir, 'dividend.csv')
        if os.path.exists(self.file_path):
            self.data = pd.read_csv(self.file_path)
        else:
            self.reload_data()

    def reload_data(self):
        data = pd.read_csv(self.file_path_raw)
        self.data = data.rename(columns={"tick": "ticker", "time": "date"})
        for index, row in self.data.iterrows():
            t = ticker_utility.get_standard_ticker(row['ticker'])
            self.data.loc[index, 'ticker'] = t
        
        self.data.to_csv(self.file_path)

    def get_data(self):
        return self.data
