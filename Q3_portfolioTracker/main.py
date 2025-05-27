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