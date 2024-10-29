import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train_model(symbol):
    print(f"Training model for {symbol}...")
    processed_data_dir = os.path.join(os.getcwd(), 'data', 'processed')
    input_path = os.path.join(processed_data_dir, f'{symbol}_stock_data_processed.csv')

    try:
        df = pd.read_csv(input_path, parse_dates=['Date'], index_col='Date')
        df['Returns'] = df['Close'].pct_change()
        df = df.dropna()

        # Feature and target
        X = df[['Open', 'High', 'Low', 'Volume']]
        y = df['Close']

        # Simple Linear Regression Model
        model = LinearRegression()
        model.fit(X, y)

        # Save the model
        models_dir = os.path.join(os.getcwd(), 'models')
        os.makedirs(models_dir, exist_ok=True)
        model_path = os.path.join(models_dir, f'{symbol}_model.pkl')
        joblib.dump(model, model_path)
        print(f"Model for {symbol} saved to {model_path}\n")
    except Exception as e:
        print(f"An error occurred while training model for {symbol}: {e}")

def main():
    company_symbols = ['NVDA', 'AMD', 'INTC']

    for symbol in company_symbols:
        train_model(symbol)

if __name__ == "__main__":
    main()
