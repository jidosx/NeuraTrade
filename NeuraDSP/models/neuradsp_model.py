# models/neuradsp_model.py
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def create_neuradsp_model():
    model = Sequential()
    model.add(LSTM(50, input_shape=(10, 1)))
    model.add(Dense(3, activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model

# models/neuradsp_model.h5
# This is the saved NeuraDSP model
