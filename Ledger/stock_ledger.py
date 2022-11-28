import pandas as pd
import os

import sys
sys.path.insert(1, '../Common')
import ticker_utility

class StockLedger:

    def __init__(self, data_dir='data'):
        self.data_dir = data_dir
        self.file_path = os.path.join(data_dir, 'stock_ledger.csv')
        self.file_path_raw = os.path.join(data_dir, 'stock_ledger_raw.csv')
        if os.path.exists(self.file_path):
            self.data = pd.read_csv(self.file_path)
        else:
            self.reload_data()

    def reload_data(self):
        data = pd.read_csv(self.file_path_raw)
        data = data[['tick', 'price', 'type', 'quantity', 'time', 'commission', 'type']]
        self.data = data.rename(columns={"tick": "ticker", "time": "date"})
        for index, row in self.data.iterrows():
            t = ticker_utility.get_standard_ticker(row['ticker'])
            self.data.loc[index, 'ticker'] = t
        
        self.data.to_csv(self.file_path)

    def get_data(self):
        return self.data

    def get_tickers(self):
        return self.data.ticker.unique().tolist()

    def get_positions(self):
        positions =  pd.DataFrame({'ticker': self.get_tickers()})
        positions['quantity'] = 0
        positions['cost'] = 0
        positions['currency'] = 'USD'
        
        for index, row in positions.iterrows():
            lots = self.get_lots(row['ticker'])
            quantity = lots[lots['type']=='buy']['quantity'].sum() - lots[lots['type']=='sell']['quantity'].sum()
            positions.loc[index, 'quantity'] = quantity

            lots['cost'] = lots['price']*lots['quantity']+lots['commission']
            avg_price = lots[lots['type']=='buy']['cost'].sum() / lots[lots['type']=='buy']['quantity'].sum()
            positions.loc[index, 'avg price'] = avg_price
            positions.loc[index, 'cost'] = avg_price * quantity

            positions.loc[index, 'currency'] = ticker_utility.get_ticker_currency(row['ticker'])

        return positions

    def get_lots(self, ticker):
        return self.data[self.data['ticker'] == ticker]
        