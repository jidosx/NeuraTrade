import alpaca_trade_api as tradeapi

class AlpacaPlugin:
    def __init__(self):
        self.api = None

    def connect_to_alpaca(self, api_key, api_secret, base_url):
        # Connect to Alpaca API
        self.api = tradeapi.REST(api_key, api_secret, base_url)

    def buy_stock(self, symbol, quantity):
        # Buy stock using Alpaca API
        self.api.submit_order(symbol, quantity, 'buy', 'market', 'day')

    def sell_stock(self, symbol, quantity):
        # Sell stock using Alpaca API
        self.api.submit_order(symbol, quantity, 'sell', 'market', 'day')
