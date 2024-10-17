import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import config

def fetch_stock_data(symbol):
    ts = TimeSeries(key=config.ALPHA_VANTAGE_API_KEY, output_format='pandas')
    data, meta_data = ts.get_daily_adjusted(symbol=symbol, outputsize='full')
    return data

if __name__ == "__main__":
    nvda_data = fetch_stock_data('NVDA')
    nvda_data.to_csv('../../data/raw/NVDA_stock_data.csv')
