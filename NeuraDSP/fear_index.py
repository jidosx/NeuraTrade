# fear_index.py
import pandas as pd
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer
from newsapi import NewsApiClient

def calculate_fear_index(news_data):
    # Calculate the fear index based on the sentiment analysis of news articles
    sia = SentimentIntensityAnalyzer()
    fear_index = 0
    for article in news_data:
        sentiment = sia.polarity_scores(article["description"])
        if sentiment["compound"] < -0.5:
            fear_index += 1
    return fear_index / len(news_data)

def get_news_data(api_key):
    # Retrieve news data from the News API
    news_api = NewsApiClient(api_key=api_key)
    news_data = news_api.get_everything(q="stock market", language="en")
    return news_data["articles"]

def update_fear_index(api_key):
    # Update the fear index based on the latest news data
    news_data = get_news_data(api_key)
    fear_index = calculate_fear_index(news_data)
    return fear_index
