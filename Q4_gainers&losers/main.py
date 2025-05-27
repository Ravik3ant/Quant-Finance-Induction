# ===================================================================== #
#                         IMPORTING MODULES                             #
# ===================================================================== #

import time
import os
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from rich import print as rprint
from rich.panel import Panel
from rich.progress import track

# ===================================================================== #
#                              CONFIG                                   #
# ===================================================================== #

confPeriod = "1mo"

# ===================================================================== #
#                      GET N SAVE PRICE DATA                            #
# ===================================================================== #

tickers = pd.read_csv("GainersNLosers/ticker.csv")["Ticker"].tolist()
data = yf.download(tickers, period=confPeriod)['Close']
daily_returns = data.pct_change() * 100
daily_returns.dropna(inplace=True)

os.makedirs("GainersNLosers/storedData", exist_ok=True)
daily_returns.to_csv("GainersNLosers/storedData/dailyReturns.csv")