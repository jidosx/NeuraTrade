import pandas as pd
from neuratrade_data import NeuraTradeData

class NeuraTradeDataPlugins:
    def __init__(self):
        self.data = NeuraTradeData()

    def yfinance_plugin(self, ticker, start_date, end_date):
        # Load data from Yahoo Finance
        self.data.load_data(ticker, start_date, end_date)
        return self.data.data

    def quandl_plugin(self, ticker, start_date, end_date):
        # Load data from Quandl
        self.data.load_data(ticker, start_date, end_date)
        return self.data.data
