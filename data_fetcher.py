import yfinance as yf
import pandas as pd

def get_historical_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data
    
