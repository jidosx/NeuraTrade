# plugins/exchanges/crypto_com.py
import requests

class CryptoComExchange:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def get_ticker(self, symbol):
        response = requests.get(f'https://api.crypto.com/v1/ticker/{symbol}')
        return response.json()

    def get_order_book(self, symbol):
        response = requests.get(f'https://api.crypto.com/v1/order-book/{symbol}')
        return response.json()
