# 📊 Quantitative Finance Induction Tasks..

This repository contains four self-contained Python mini-projects focused on algorithmic trading and financial analysis using real-time market data via `yfinance`.

Each project emphasizes hands-on experience with financial concepts such as technical indicators, volatility, portfolio tracking, and performance comparison.

---

## 📁 Project Structure

```
.
├── GainersNLosers
│   └── main.py
│   └── requirements.txt
│   └── ticker.csv
├── Portfolio Tracker (Incomplete)
│   └── main.py
│   └── requirements.txt
├── SMA
│   └── main.py
│   └── requirements.txt
│   └── ticker.csv
├── StatsNAnalysis
│   └── main.py
│   └── requirements.txt
│   └── ticker.csv
├── .gitignore
└── README.md
```

---

## 📈 Q1: Simple Moving Average (SMA) Crossover Strategy

**Objective**: Implement a basic trading strategy using 5-day and 20-day SMAs.

### ✅ Features
- Download 6 months of stock data via `yfinance`.
- Calculate 5-day and 20-day SMAs.
- Generate Buy/Sell signals using SMA crossovers.
- Visualize:
  - Stock closing price
  - 5-day SMA & 20-day SMA
  - Buy/Sell points on the chart
- Uses `matplotlib`, `rich`, and animated console output for UX.

### 🛠️ How to Run
```bash
python Q1_SMA_Crossover.py
```

---

## 📉 Q2: Rolling Statistics & Volatility Analysis

**Objective**: Analyze stock return behavior and volatility over time.

### ✅ Features
- Fetch 3–6 months of historical data.
- Calculate:
  - Daily Returns
  - 7-day Rolling Mean
  - 7-day Rolling Standard Deviation (volatility)
- All 3 metrics are plotted on one chart for interpretation.

### 🧠 Insights
This helps understand how volatile a stock is and how its return behavior changes over time — critical for risk assessment.

### 🛠️ How to Run
```bash
python Q2_RollingVolatility.py
```

---

## 💼 Q3: Portfolio Value Tracker

**Objective**: Track total portfolio value over the last 30 days.

### ✅ Features
- Define a sample portfolio (tickers + number of shares).
- Fetch adjusted closing prices.
- Compute total portfolio value daily.
- Plot the value over time.
- Print the latest total portfolio value.

### 🛠️ How to Run
```bash
python Q3_Portfolio_Tracker.py
```

---

## 🚀 Q4: Gainers & Losers Scanner

**Objective**: Identify top 5 gainers and losers in a group of stocks.

### ✅ Features
- Download 1 month of data for 20 Nifty 50 stocks.
- Compute % change in adjusted closing prices.
- Identify top 5 gainers and top 5 losers.
- Plot a bar chart (color-coded).
- Save results to `gainers_losers.csv`.

### 📊 Output
- A clean visual comparing winners and losers
- CSV export with stock name and % change

### 🛠️ How to Run
```bash
python Q4_Gainers_Losers_Scanner.py
```

---

## 🔧 Dependencies

Install all required packages using:

```bash
pip install -r requirements
```

> Note: `matplotlib` may require a display backend for Linux systems. You can use Jupyter Notebooks or install GUI packages like `Tkinter` if `plt.show()` fails.

---

## 📎 Notes

- All scripts handle exceptions and missing data gracefully.
- Code is modular and easy to expand with more strategies or indicators.
- Internet connection is required for live data fetching via `yfinance`.

---

## 👨‍💻 Author

Made with ❤️ by [Ravi @ BITS Hyderabad]

---

## 🧠 Suggestions or Contributions?

Feel free to open a pull request or file an issue for ideas, bugs, or improvements.
