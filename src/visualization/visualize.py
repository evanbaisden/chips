import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_stock_prices(symbol):
    print(f"Plotting stock prices for {symbol}...")
    processed_data_dir = os.path.join(os.getcwd(), 'data', 'processed')
    input_path = os.path.join(processed_data_dir, f'{symbol}_stock_data_processed.csv')

    try:
        df = pd.read_csv(input_path, parse_dates=['Date'], index_col='Date')
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df, x=df.index, y='Close')
        plt.title(f"{symbol} Stock Prices Over Time")
        plt.xlabel('Date')
        plt.ylabel('Close Price USD')
        figures_dir = os.path.join(os.getcwd(), 'reports', 'figures')
        os.makedirs(figures_dir, exist_ok=True)
        output_path = os.path.join(figures_dir, f'{symbol}_stock_price.png')
        plt.savefig(output_path)
        plt.close()
        print(f"Plot saved to {output_path}\n")
    except Exception as e:
        print(f"An error occurred while plotting {symbol}: {e}")

def main():
    company_symbols = ['NVDA', 'AMD', 'INTC']

    for symbol in company_symbols:
        plot_stock_prices(symbol)

if __name__ == "__main__":
    main()
