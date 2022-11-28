from datetime import date
import os
import pandas as pd
from yahoo_fin.stock_info import get_data

class Yahoo_Fin:

    def __init__(self, ticker, start_date="1900-1-1", end_date=date.today(), data_dir='data/stock_price') -> None:
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
        self.file_path = os.path.join(data_dir, ticker +'.csv')

    def __ensure_has_data(self):
        if os.path.exists(self.file_path):
            self.data = pd.read_csv(self.file_path)
        else:
            self.reload_data()

    def reload_data(self):
        data = get_data(self.ticker, start_date=self.start_date, end_date=self.end_date, index_as_date = True, interval="1d")
        self.data = data[['ticker', 'adjclose']]
        self.data.to_csv(self.file_path)

    def get_price(self):
        self.__ensure_has_data()
        return self.data

    def get_last_price(self):
        price = self.get_price()
        return price.iloc[-1]['adjclose']

    def save(self):
        self.__ensure_has_data()

