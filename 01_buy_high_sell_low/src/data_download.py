# ==========================
# IMPORTS
# ==========================
import yfinance as yf
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
import os

# ==========================
# CONFIGURATIONS
# ==========================
print('List of Top 50 tickers \n') 
TICKERS = [
    'AAPL', 'MSFT', 'GOOG', 'AMZN', 'META', 'TSLA', 'NVDA', 'BRK-B', 'V', 'JPM',
    'UNH', 'XOM', 'PG', 'MA', 'HD', 'CVX', 'MRK', 'ABBV', 'PEP', 'KO',
    'COST', 'LLY', 'AVGO', 'MCD', 'WMT', 'BAC', 'VZ', 'ADBE', 'CSCO', 'PFE',
    'TMO', 'ABT', 'NFLX', 'ACN', 'CRM', 'DHR', 'INTC', 'NKE', 'TXN', 'WFC',
    'LIN', 'ORCL', 'BMY', 'QCOM', 'NEE', 'MDT', 'HON', 'PM', 'UPS'
]

# Dynamic date range: last 5 years
END_DATE = datetime.today()
START_DATE = END_DATE - timedelta(days=5*365)

# Data save path
SAVE_PATH = "../data/top_50_stock_data.csv"

# ==========================
# FUNCTIONS
# ==========================
print('Download Stock data \n')
def fetch_stock_data(ticker):
    try:
        print(f"Fetching {ticker} ...")
        stock = yf.download(
            ticker,
            start=START_DATE.strftime("%Y-%m-%d"),
            end=END_DATE.strftime("%Y-%m-%d"),
            interval="1d",
            progress=False,
            auto_adjust=True,   # Adjust for splits/dividends
            threads=False       # Required for manual ThreadPoolExecutor
        )
        stock['Ticker'] = ticker
        return stock
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")
        return None

# ==========================
# MAIN PIPELINE
# ==========================
def main():
    all_data = []

    # Thread Pool for Parallel Download
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_stock_data, ticker): ticker for ticker in TICKERS}
        for future in as_completed(futures):
            data = future.result()
            if data is not None and not data.empty:
                all_data.append(data)

    # Combine all into a single DataFrame
    if all_data:
        final_df = pd.concat(all_data)
        final_df.reset_index(inplace=True)

        # Save to CSV
        final_df.to_csv(SAVE_PATH, index=False)
        print(f"\n✅ Download complete! Data saved to '{SAVE_PATH}'")
    else:
        print("\n⚠️ No data downloaded.")

# ==========================
# ENTRY POINT
# ==========================
if __name__ == "__main__":
    # Create output folder if needed
    os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
    main()
