import numpy as np
from neuratrade_models import NeuraTradeModels

class NeuraTradeModelsPlugins:
    def __init__(self):
        self.model = NeuraTradeModels()

    def lstm_plugin(self, data):
        # Create an LSTM model
        self.model.create_model()
        # Train the model using the provided data
        self.model.train_model(data)
        # Make predictions using the trained model
        return self.model.predict(data)

    def gru_plugin(self, data):
        # Create a GRU model
        self.model.create_model()
        # Train the model using the provided data
        self.model.train_model(data)
        # Make predictions using the trained model
        return self.model.predict(data)
