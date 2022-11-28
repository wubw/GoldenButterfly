from datetime import datetime, timedelta
from query import *
from yahoo_fin_ import *

class Ingestor:

    def __init__(self, ticker, data_dir='data'):
        self.ticker = ticker
        self.data_dir = data_dir

    def update_data(self):
        query = Query(self.ticker, self.data_dir)
        lastdate = query.get_last_date()
        lastdate = datetime.strptime(lastdate, r"%Y-%m-%d").date()
        startdate = lastdate + timedelta(days=1)
        yf = Yahoo_Fin(self.ticker, startdate, data_dir=self.data_dir)
        data = yf.get_price()
        data.to_csv(yf.file_path, mode='a', header=False)
