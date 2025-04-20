import pandas as pd
import numpy as np
import os

# Parameters
PCT_CHANGE_THRESHOLD = 0.02  # +2% move
HOLD_DAYS = 5

# Load Data
DATA_PATH = "/Users/ananyapattnaik/Desktop/ml-course/AlgoTrading/01_buy_high_sell_low/data/Clean_Ticker_data.csv"
df = pd.read_csv(DATA_PATH, parse_dates=['Date'])

# Preprocessing
df.sort_values(['Ticker', 'Date'], inplace=True)

# Calculate Daily Returns
df['Pct_Change'] = df.groupby('Ticker')['Close'].pct_change()

# Generate Buy Signals
df['Buy_Signal'] = df['Pct_Change'] > PCT_CHANGE_THRESHOLD

# Simulate Trading
trades = []

for ticker, ticker_df in df.groupby('Ticker'):
    ticker_df = ticker_df.reset_index(drop=True)
    for i, row in ticker_df.iterrows():
        if row['Buy_Signal']:
            entry_idx = i + 1  # Next day
            exit_idx = entry_idx + HOLD_DAYS

            if exit_idx < len(ticker_df):
                entry_price = ticker_df.loc[entry_idx, 'Open']
                exit_price = ticker_df.loc[exit_idx, 'Close']
                pnl = (exit_price - entry_price) / entry_price

                trades.append({
                    'Ticker': ticker,
                    'Entry_Date': ticker_df.loc[entry_idx, 'Date'],
                    'Exit_Date': ticker_df.loc[exit_idx, 'Date'],
                    'PnL': pnl
                })

# Convert to DataFrame
trades_df = pd.DataFrame(trades)

# Save
trades_df.to_csv("../data/buy_high_sell_low_trades.csv", index=False)

print("Backtest complete. Saved trades.")
