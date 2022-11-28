import requests
import os
import json
from datetime import datetime
from datetime import date

class ExchangeRateHost:

    def __init__(self, data_dir='data/exchange_rate') -> None:
        self.data_dir = data_dir
        self.cache = {}

    def get_exchangerate_raw(self, start_date, end_date, symbols):
        url = f'https://api.exchangerate.host/timeseries'
        payload = {'start_date': start_date, 'end_date': end_date, 'symbols':symbols}
        response = requests.get(url, params=payload)
        data = response.json()
        return data

    def get_exchangerate_raw_yearly(self, year, symbols):
        current_year = date.today().year
        start_date = str(year) + '-01-01'
        end_date = None
        file_path = self.data_dir + '/' + str(year) + '.json'
        if year != current_year:
            if os.path.exists(file_path):
                data = json.load(open(file_path))
                return data
            else:
                end_date = str(year) + '-12-31'
        else:
            now = datetime.now()
            m = now.strftime('%m')
            d = now.strftime('%d')
            end_date = str(year) + '-' + m + '-' + d

        data = self.get_exchangerate_raw(start_date, end_date, symbols)
        json_object = json.dumps(data, indent=4)
        with open(file_path, "w") as outfile:
            outfile.write(json_object)
        return data

    def get_exchange_rate(self, from_, to_, date_=date.today()):
        if date_ > date.today():
            raise ValueError('date should not be later than today.')
        padding_date_str = date_.strftime("%Y-%m-%d")
        key = from_ + ',' + to_ + ',' + padding_date_str
        if key in self.cache:
            return self.cache[key]

        data = self.get_exchangerate_raw_yearly(date_.year, 'NOK,USD,SGD,CNY,HKD')

        f = data['rates'][padding_date_str][from_]
        t = data['rates'][padding_date_str][to_]
        v = t/f
        self.cache[key] = v
        return v

