# neuradsp/deepseek_algorithms/lstm_predictor.py
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class LSTM_Predictor:
    def __init__(self, input_shape, output_shape):
        self.model = Sequential()
        self.model.add(LSTM(50, input_shape=input_shape))
        self.model.add(Dense(output_shape))
        self.model.compile(loss='mean_squared_error', optimizer='adam')

    def predict(self, data):
        return self.model.predict(data)
