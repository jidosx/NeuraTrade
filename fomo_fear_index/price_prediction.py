# fomo_fear_index/price_prediction.py
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

class PricePrediction:
    def __init__(self, historical_data):
        self.historical_data = pd.DataFrame(historical_data)

    def predict(self, input_data):
        model = RandomForestRegressor()
        model.fit(self.historical_data.drop('price', axis=1), self.historical_data['price'])
        return model.predict(input_data)
