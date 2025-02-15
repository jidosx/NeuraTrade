import unittest
from neuratrade.plugin.alpaca import AlpacaPlugin
import alpaca_trade_api as tradeapi

class TestAlpacaPlugin(unittest.TestCase):
    def test_connect_to_alpaca(self):
        # Create Alpaca plugin
        alpaca_plugin = AlpacaPlugin()

        # Connect to Alpaca API
        alpaca_plugin.connect_to_alpaca('api_key', 'api_secret', 'https://paper-api.alpaca.markets')

        # Check if the connection is established
        self.assertIsNotNone(alpaca_plugin.api)

    def test_buy_stock(self):
        # Create Alpaca plugin
        alpaca_plugin = AlpacaPlugin()

        # Connect to Alpaca API
        alpaca_plugin.connect_to_alpaca('api_key', 'api_secret', 'https://paper-api.alpaca.markets')

        # Buy stock using Alpaca API
        alpaca_plugin.buy_stock('AAPL', 10)

        # Check if the stock is bought
        self.assertIsNotNone(alpaca_plugin.api.get_position('AAPL'))

    def test_sell_stock(self):
        # Create Alpaca plugin
        alpaca_plugin = AlpacaPlugin()

        # Connect to Alpaca API
        alpaca_plugin.connect_to_alpaca('api_key', 'api_secret', 'https://paper-api.alpaca.markets')

        # Buy stock using Alpaca API
        alpaca_plugin.buy_stock('AAPL', 10)

        # Sell stock using Alpaca API
        alpaca_plugin.sell_stock('AAPL', 10)

        # Check if the stock is sold
        self.assertIsNone(alpaca_plugin.api.get_position('AAPL'))

if __name__ == '__main__':
    unittest.main()
