import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def fetch_stock_data(symbol):
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    if not api_key:
        raise ValueError("ALPHA_VANTAGE_API_KEY is not set. Please check your .env file.")
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, _ = ts.get_daily_adjusted(symbol=symbol, outputsize='full')
    return data

if __name__ == "__main__":
    # Fetch data for NVIDIA
    nvda_data = fetch_stock_data('NVDA')

    # Determine the output directory
    output_dir = os.path.join(os.getcwd(), 'data', 'raw')
    os.makedirs(output_dir, exist_ok=True)

    # Save the data to a CSV file
    output_path = os.path.join(output_dir, 'NVDA_stock_data.csv')
    nvda_data.to_csv(output_path)
    print(f"Data saved to {output_path}")
