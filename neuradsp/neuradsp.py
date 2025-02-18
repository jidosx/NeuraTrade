# neuradsp/neuradsp.py
from neuradsp.deepseek_algorithms import LSTM_Predictor, GRU_Regressor

class NeuraDSP:
    def __init__(self, model_type, **kwargs):
        if model_type == 'lstm':
            self.model = LSTM_Predictor(**kwargs)
        elif model_type == 'gru':
            self.model = GRU_Regressor(**kwargs)
        else:
            raise ValueError('Invalid model type')

    def predict(self, data):
        return self.model.predict(data)
