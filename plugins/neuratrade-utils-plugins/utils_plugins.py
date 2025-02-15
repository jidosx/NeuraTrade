import numpy as np
from neuratrade_utils import NeuraTradeUtils

class NeuraTradeUtilsPlugins:
    def __init__(self):
        self.utils = NeuraTradeUtils()

    def sharpe_ratio_plugin(self, returns):
        # Calculate the Sharpe ratio
        return self.utils.calculate_sharpe_ratio(returns)

    def sortino_ratio_plugin(self, returns):
        # Calculate the Sortino ratio
        return self.utils.calculate_sortino_ratio(returns)
