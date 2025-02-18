# plugins/brokers/binance.py
import ccxt

class BinanceBroker:
    def __init__(self, api_key, api_secret):
        self.exchange = ccxt.binance({
            'apiKey': api_key,
            'apiSecret': api_secret,
        })

    def get_balance(self):
        return self.exchange.fetch_balance()

    def place_order(self, symbol, side, amount, price):
        return self.exchange.create_order(symbol, 'limit', side, amount, price)
