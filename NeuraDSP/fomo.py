# fomo.py
import pandas as pd
import numpy as np
from fear_index import update_fear_index

def calculate_fomo(fear_index, market_data):
    # Calculate FOMO based on the fear index and market data
    fomo = 0
    if fear_index > 0.5:
        fomo += 1
    if market_data["close"] > market_data["open"]:
        fomo += 1
    return fomo / 2

def update_fomo(api_key, market_data):
    # Update FOMO based on the latest fear index and market data
    fear_index = update_fear_index(api_key)
    fomo = calculate_fomo(fear_index, market_data)
    return fomo
