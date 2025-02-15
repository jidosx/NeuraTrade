import numpy as np

class NeuraTradeUtils:
    def __init__(self):
        pass

    def calculate_sharpe_ratio(self, returns):
        # Calculate the Sharpe ratio
        sharpe_ratio = np.mean(returns) / np.std(returns)
        return sharpe_ratio

    def calculate_sortino_ratio(self, returns):
        # Calculate the Sortino ratio
        sortino_ratio = np.mean(returns) / np.std(returns)
        return sortino_ratio
