📈 Algo Trading Project: Top 50 US Stocks Strategy

- This project builds an end-to-end algorithmic trading backtest system.
- It downloads and processes historical stock data for the top 50 US companies, simulates a basic momentum-based trading strategy, and outputs the results.

🚀 Project Goal

- Download 5 years of historical daily stock data for the top 50 US stocks.
- Preprocess and clean the data.
- Detect +2% daily move as a buy signal.
- Simulate buying at next day's open and selling after 5 trading days.
- Analyze and export simulated trading results.

## 🛠 Tech Stack

- Python (Core programming)
- yfinance (Download stock price data)
- pandas (Data manipulation)
- numpy (Numerical operations)
- concurrent.futures (parallel data download)

## 📂 Folder Structure

```
algo-trading-project/ ├── data/ # Downloaded CSV data ├── notebooks/ # Jupyter notebooks ├── src/ # Python source code ├── README.md # Documentation ├── requirements.txt # Dependencies └── .gitignore # Git settings
```
