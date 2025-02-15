import numpy as np
from neuratrade_strategies import NeuraTradeStrategies

class NeuraTradeStrategiesPlugins:
    def __init__(self):
        self.strategy = NeuraTradeStrategies()

    def mean_reversion_strategy_plugin(self, data):
        # Execute the mean reversion strategy
        return self.strategy.execute_strategy(data)

    def bollinger_bands_strategy_plugin(self, data):
        # Execute the Bollinger Bands strategy
        return self.strategy.execute_strategy(data)
