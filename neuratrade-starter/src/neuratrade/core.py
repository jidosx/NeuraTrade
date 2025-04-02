import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

class NeuraTradeCore:
    def __init__(self):
        self.model = None

    def train(self, data):
        # Train the model using the provided data
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(data)
        X = []
        y = []
        for i in range(60, len(scaled_data)):
            X.append(scaled_data[i-60:i, 0])
            y.append(scaled_data[i, 0])
        X, y = np.array(X), np.array(y)
        X = np.reshape(X, (X.shape[0], X.shape[1], 1))
        self.model = Sequential()
        self.model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
        self.model.add(LSTM(50, return_sequences=False))
        self.model.add(Dense(25))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam', loss='mean_squared_error')
        self.model.fit(X, y, batch_size=1, epochs=1)

    def predict(self, input_data):
        # Make predictions using the trained model
        return self.model.predict(input_data)

