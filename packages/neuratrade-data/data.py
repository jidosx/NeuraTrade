import pandas as pd
import yfinance as yf

class NeuraTradeData:
    def __init__(self):
        self.data = None

    def load_data(self, ticker, start_date, end_date):
        # Load data from Yahoo Finance
        self.data = yf.download(ticker, start=start_date, end=end_date)

    def preprocess_data(self):
        # Preprocess the data
        self.data['Date'] = pd.to_datetime(self.data.index)
        self.data['Date'] = self.data['Date'].apply(lambda date: date.timestamp())
        self.data.set_index('Date', inplace=True)
        return self.data
