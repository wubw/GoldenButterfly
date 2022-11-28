from flask import Flask, request
from markupsafe import escape
from yahoo_fin_ import *
from exchangerate import *

app = Flask(__name__)

@app.route("/stock/last_price/<ticker>")
def stock_last_price(ticker):
    ticker = escape(ticker)
    yahoo_fin = Yahoo_Fin(ticker)
    return f"{yahoo_fin.get_last_price()}"

@app.route("/exchange_rate")
def exchange_rate():
    from_ = request.args.get('from', None)
    to_ = request.args.get('to', None)
    d = request.args.get('date', None)
    er = ExchangeRateHost()
    return f"{er.get_exchange_rate(from_, to_)}"
