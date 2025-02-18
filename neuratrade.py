# neuratrade.py
import numpy as np
from ctypes import CDLL

# Load the Assembly x86 code
lib = CDLL('./neuratrade.so')

# Define the trading strategy
def trading_strategy(stock_price):
    # Call the Assembly x86 code
    lib._start()
    # Get the buy and sell signals
    buy_signal = lib.buy_signal
    sell_signal = lib.sell_signal
    # Return the signals
    return buy_signal, sell_signal

# Use the trading strategy
stock_price = 100.0
buy_signal, sell_signal = trading_strategy(stock_price)
print(f'Buy signal: {buy_signal}')
print(f'Sell signal: {sell_signal}')
