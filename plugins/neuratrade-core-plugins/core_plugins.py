import numpy as np
from neuratrade_core import NeuraTradeCore

class NeuraTradeCorePlugins:
    def __init__(self):
        self.core = NeuraTradeCore()

    def mean_reversion_plugin(self, data):
        # Calculate the mean reversion
        mean = np.mean(data)
        std_dev = np.std(data)
        upper_bound = mean + 2 * std_dev
        lower_bound = mean - 2 * std_dev
        # Check if the data is above or below the bounds
        if data > upper_bound:
            return 'sell'
        elif data < lower_bound:
            return 'buy'
        else:
            return 'hold'

    def bollinger_bands_plugin(self, data):
        # Calculate the Bollinger Bands
        mean = np.mean(data)
        std_dev = np.std(data)
        upper_band = mean + 2 * std_dev
        lower_band = mean - 2 * std_dev
        # Check if the data is above or below the bands
        if data > upper_band:
            return 'sell'
        elif data < lower_band:
            return 'buy'
        else:
            return 'hold'
