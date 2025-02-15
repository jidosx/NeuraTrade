import torch
import torch.nn as nn
from .base_model import BaseModel

class NeuralNetwork(BaseModel):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(5, 10),  # Input layer (5) -> Hidden layer (10)
            nn.ReLU(),
            nn.Linear(10, 5)   # Hidden layer (10) -> Output layer (5)
        )

    def train(self, data):
        # TO DO: Implement training logic
        pass

    def predict(self, data):
        # TO DO: Implement prediction logic
        pass
