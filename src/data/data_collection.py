import os
import pandas as pd
import yfinance as yf
from dotenv import load_dotenv
import time

# Load environment variables
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
dotenv_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path=dotenv_path)

def fetch_stock_data(symbol):
    print(f"Fetching stock data for {symbol}...")
    data = yf.download(symbol, period='max')
    return data

def main():
    # List of semiconductor companies
    company_symbols = ['NVDA', 'AMD', 'INTC', 'TSM', 'ASML', 'QCOM', 'MU', 'AVGO', 'TXN']

    raw_data_dir = os.path.join(project_root, 'data', 'raw')
    os.makedirs(raw_data_dir, exist_ok=True)

    for symbol in company_symbols:
        try:
            stock_data = fetch_stock_data(symbol)
            output_path = os.path.join(raw_data_dir, f'{symbol}_stock_data.csv')
            stock_data.to_csv(output_path)
            print(f"Data for {symbol} saved to {output_path}\n")
            time.sleep(1)  # Sleep to prevent overloading the API
        except Exception as e:
            print(f"An error occurred for {symbol}: {e}")

if __name__ == "__main__":
    main()
