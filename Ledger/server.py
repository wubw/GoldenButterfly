from flask import Flask
from stock_ledger import *

app = Flask(__name__)

@app.route("/positions")
def get_positions():
    stocker_ledger = StockLedger()
    positions = stocker_ledger.get_positions()
    return positions.to_json()
