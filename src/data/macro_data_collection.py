import os
import pandas as pd
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
project_root = os.getenv('PROJECT_ROOT')

# Define data directory
raw_data_dir = os.path.join(project_root, 'data', 'raw')
os.makedirs(raw_data_dir, exist_ok=True)

# Function to fetch data from FRED
def fetch_fred_data(series_id, api_key):
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"
    response = requests.get(url)
    data = response.json()
    observations = data['observations']
    df = pd.DataFrame(observations)
    df['date'] = pd.to_datetime(df['date'])
    df = df[['date', 'value']]
    df.rename(columns={'value': series_id}, inplace=True)
    return df

def main():
    api_key = os.getenv('FRED_API_KEY')
    if not api_key:
        raise ValueError("FRED_API_KEY not found in environment variables.")

    fred_series = {
        'GDP': 'GDP',
        'CPI': 'CPIAUCSL',
        'UNRATE': 'UNRATE',
        'FEDFUNDS': 'FEDFUNDS',
    }

    data_frames = []
    for name, series_id in fred_series.items():
        print(f"Fetching {name} data from FRED...")
        df = fetch_fred_data(series_id, api_key)
        df.set_index('date', inplace=True)
        data_frames.append(df)

    # Merge all dataframes on date
    macro_df = pd.concat(data_frames, axis=1)
    macro_df.to_csv(os.path.join(raw_data_dir, 'macro_data.csv'))
    print("Macroeconomic data saved successfully.")

if __name__ == "__main__":
    main()
