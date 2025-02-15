import unittest
from neuratrade.models.lstm import LSTMModel
import numpy as np

class TestLSTMModel(unittest.TestCase):
    def test_train(self):
        # Create LSTM model
        lstm_model = LSTMModel()

        # Create random data
        data = np.random.rand(100, 1)

        # Train the model
        lstm_model.train(data)

        # Check if the model is trained
        self.assertIsNotNone(lstm_model.model)

    def test_predict(self):
        # Create LSTM model
        lstm_model = LSTMModel()

        # Create random data
        data = np.random.rand(100, 1)

        # Train the model
        lstm_model.train(data)

        # Make predictions
        predictions = lstm_model.predict(data)

        # Check if the predictions are made
        self.assertIsNotNone(predictions)

if __name__ == '__main__':
    unittest.main()
