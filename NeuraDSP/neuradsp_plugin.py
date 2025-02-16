import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
from iNeuraTrade import BasePlugin

class NeuraDSPPlugin(BasePlugin):
    def __init__(self, model_path, deepseek_api_key):
        self.model_path = model_path
        self.deepseek_api_key = deepseek_api_key
        self.model = None
        self.scaler = None

    async def initialize(self):
        # Load the NeuraDSP model
        self.model = load_model(self.model_path)

        # Initialize the Min-Max Scaler
        self.scaler = MinMaxScaler()

    async def process(self, trading_context):
        # Get the market data from the trading context
        market_data = trading_context.data["market_data"]

        # Scale the market data
        scaled_data = self.scaler.fit_transform(market_data)

        # Make predictions using the NeuraDSP model
        predictions = self.model.predict(scaled_data)

        # Get the predicted trends
        trends = np.argmax(predictions, axis=1)

        # Create a dictionary with the predicted trends
        trend_dict = {"trend": trends}

        # Update the trading context with the predicted trends
        trading_context.data["predicted_trends"] = trend_dict

        return trading_context

    def can_handle(self, trading_context):
        return "market_data" in trading_context.data and "predicted_trends" not in trading_context.data
