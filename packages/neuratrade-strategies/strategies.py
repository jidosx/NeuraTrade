import numpy as np

class NeuraTradeStrategies:
    def __init__(self):
        self.strategy = None

    def create_strategy(self):
        # Create a new strategy
        self.strategy = 'mean_reversion'

    def execute_strategy(self, data):
        # Execute the strategy using the provided data
        if self.strategy == 'mean_reversion':
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
