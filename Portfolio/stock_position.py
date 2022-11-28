ingestion_service_url = "http://127.0.0.1:5001"
ledger_service_url = "http://127.0.0.1:5000"

import requests
import pandas as pd
import json
from settings import *
from dividend import *

class StockPosition:

    def __init__(self):
        self.settings = Settings()

    def get_positions(self):
        response = requests.get(ledger_service_url + "/positions")
        dict= json.loads(response.content)
        positions = pd.DataFrame.from_dict(dict, orient="columns")

        positions['last price'] = 0
        positions['currency rate'] = 1
        exchange_rate_cache = {}

        d = Dividend()
        dividend_data = d.get_data()
        positions['dividend'] = 0
        for index, row in positions.iterrows():
            ticker = row['ticker']
            response = requests.get(ingestion_service_url + "/stock/last_price/" + ticker)
            positions.loc[index, 'last price'] = float(response.content)

            from_currency = row['currency']
            to_currency = self.settings.base_currency
            key = from_currency + ',' + to_currency
            exchange_rate = 0

            positions.loc[index, 'dividend'] = dividend_data[dividend_data['ticker'] == ticker]['amount'].sum()

            if key in exchange_rate_cache:
                exchange_rate = exchange_rate_cache[key]
            else:
                response2 = requests.get(ingestion_service_url + "/exchange_rate?" + f'from={from_currency}&to={to_currency}')
                exchange_rate = float(response2.content)
                exchange_rate_cache[key] = exchange_rate
            positions.loc[index, 'currency rate'] = exchange_rate

        positions['cur value'] = positions['quantity'] * positions['last price']
        positions['change'] = positions['cur value'] - positions['cost'] + positions['dividend']
        positions['return'] = positions['change'] / positions['cost']
        positions['change (conv)'] = positions['change'] * positions['currency rate']

        positions['cur value (conv)'] = positions['cur value'] * positions['currency rate']
        positions['allocation'] = positions['cur value (conv)'] / positions['cur value (conv)'].sum()
        print(positions)
        return positions
