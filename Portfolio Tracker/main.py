# ===================================================================== #
#                         IMPORTING MODULES                             #
# ===================================================================== #

import os
import time
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as pl
import rich 
from rich.panel import Panel
from rich.progress import track

# ===================================================================== #
#                     PORTFOLIO & CONFIGURATION                         #
# ===================================================================== #

portfolio = {
    "INFY.NS": 15,
    "TCS.NS":10,
    "RELIANCE.NS":12
}
period="30d"

# ===================================================================== #
#                         LOAD TICKER DATA                              #
# ===================================================================== #

data = {}
for ticker in portfolio:
    try:
        rich.print(f"[yellow]Loading {ticker}...", end="")
        df = yf.download(ticker, period=period)['Adj Close']

        for _ in track(range(10), description="LOADING DATA..."):
            time.sleep(0.2)

        if df.empty:
            raise ValueError(f"No data for {ticker}")
        data[ticker] = df
        rich.print(f"[green] Success")
    except Exception as e:
        rich.print(f"[red] Failed: {e}")

# ===================================================================== #
#                         LOAD TICKER DATA                              #
# ===================================================================== #

if not data:
    rich.print("[bold red]No valid data fetched. Exiting.")
    exit()

portfolioData = pd.DataFrame(data)
# for ticker, shares in portfolio.items():
#     if ticker in portfolioData.columns:
print(portfolioData)
print(data)