import streamlit as st
import pandas as pd
import os

def load_data(symbol):
    processed_data_dir = os.path.join(os.getcwd(), 'data', 'processed')
    input_path = os.path.join(processed_data_dir, f'{symbol}_stock_data_processed.csv')
    df = pd.read_csv(input_path, parse_dates=['Date'], index_col='Date')
    return df

def main():
    st.title("Semiconductor Industry Analysis Dashboard")

    company_symbols = ['NVDA', 'AMD', 'INTC']
    symbol = st.sidebar.selectbox("Select a Company", company_symbols)

    df = load_data(symbol)

    st.subheader(f"{symbol} Stock Prices")
    st.line_chart(df['Close'])

    st.subheader(f"{symbol} Data Overview")
    st.write(df.describe())

if __name__ == "__main__":
    main()
