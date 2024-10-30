import os
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def preprocess_stock_data(symbol):
    print(f"Preprocessing data for {symbol}...")

    # Get the project root from the environment variable
    project_root = os.getenv('PROJECT_ROOT')
    if not project_root:
        raise ValueError("PROJECT_ROOT environment variable not set.")
    print(f"Project root: {project_root}")

    # Construct the paths
    raw_data_dir = os.path.join(project_root, 'data', 'raw')
    processed_data_dir = os.path.join(project_root, 'data', 'processed')
    os.makedirs(processed_data_dir, exist_ok=True)

    input_path = os.path.join(raw_data_dir, f'{symbol}_stock_data.csv')
    output_path = os.path.join(processed_data_dir, f'{symbol}_stock_data_processed.csv')

    print(f"Input path for {symbol}: {input_path}")

    try:
        df = pd.read_csv(input_path, parse_dates=['Date'], index_col='Date')
        df = df.dropna()
        df.to_csv(output_path)
        print(f"Processed data for {symbol} saved to {output_path}\n")
    except Exception as e:
        print(f"An error occurred while preprocessing {symbol}: {e}")

def main():
    company_symbols = ['NVDA', 'AMD', 'INTC', 'TSM', 'ASML', 'QCOM', 'MU', 'AVGO', 'TXN']

    for symbol in company_symbols:
        preprocess_stock_data(symbol)

if __name__ == "__main__":
    main()
