def get_standard_ticker(t):
    if t.isdigit():
        if len(t) == 4:
            t = t + '.HK'
        elif len(t) == 6:
            t = t + '.SS'
    return t

def get_ticker_currency(ticker):
    if ticker.endswith('.SI'):
        return 'SGD'
    elif ticker.endswith('.SS'):
        return 'CNY'
    elif ticker.endswith('.HK'):
        return 'HKD'
    else:
        return 'USD'
