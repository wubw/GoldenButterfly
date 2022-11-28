import pandas as pd
import os

class Query:
    
    def __init__(self, ticker, data_dir='data'):
        self.ticker = ticker
        self.file_path = os.path.join(data_dir, ticker +'.csv')
        self.df = pd.read_csv(self.file_path)
        self.df = self.df.rename(columns={"Unnamed: 0": "date"})

    def get_last_price(self):
        return self.df.iloc[-1]['adjclose']

    def get_last_date(self):
        return self.df.iloc[-1]['date']
