# ===================================================================== #
#                         IMPORTING MODULES                             #
# ===================================================================== #

import os
import time
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import rich
from rich import print as rprint
from rich.panel import Panel
from rich.progress import track

# ==================================================================== #
#             GLOABAL VARIABLES(IDK why this exists)                   #
# ==================================================================== #

retries = 3

# ==================================================================== #
#                  LOADING THE DATA FROM CSV FILE                      #
# ==================================================================== #

tickerList = pd.read_csv("StatsNAnalysis/tickers.csv")

# ==================================================================== #
#                  SELECTION OF COMPANY BY USER                        #
# ==================================================================== #

rich.print(f"[#DFF2F8]{tickerList}")
try:
    tickerSelector = int(input("Enter a Number b/w 0 - 9 to Select a Company: "))
    if tickerSelector < 0 or tickerSelector > 9:
        raise ValueError("Invalid input! Please enter a number between 0 and 9.")
    # You can continue using tickerSelector here
    print("You selected:", tickerSelector)
except ValueError as e:
    rich.print(f"[bold red]ERROR: {e}")

# ==================================================================== #
#               GET OR DOWNLOAD DATA FROM YFINANCE                     #
# ==================================================================== #

ticker = tickerList['Ticker'][tickerSelector]
for attempt in range(1,retries+1):
    try:
        rich.print(f"[bold yellow][ATTEMPT] {attempt} Downloading {tickerList['Company Name'][tickerSelector]} data")
        data = yf.download(ticker,period="6mo")
        for step in track(range(10), description="LOADING DATA..."):
            time.sleep(0.2)

        if data.empty:
            raise ValueError(f"No Data found for ticker: {tickerList['Company Name'][tickerSelector]}")
        
        rich.print(f"[bold green] SUCCESS: {tickerList['Company Name'][tickerSelector]} value generated")
        break
        
    except ValueError as ve:
        rich.print(f"[bold red]: {ve}")
        break
    except Exception as e:
        rich.print(f"[bold red] Error Downloading {tickerList['Company Name'][tickerSelector]}: {e}  ")
        if attempt < retries:
            rich.print(f"[bold yellow] Retrying...")
            time.sleep(1.5)
        else: 
            rich.print(f"[bold red] Failed After Multiple Attempts.")

# ==================================================================== #
#               COMPUTE RETURNS, MEAN AND STD. DEV                     #
# ==================================================================== #

data['Daily Return'] = data['Close'].pct_change()*100 
data['Rolling Mean'] = (data['Daily Return']/100).rolling(window=7).mean()
data['Rolling Std'] = (data['Daily Return']/100).rolling(window=7).std()

data = data.dropna() # DROPS ALL NAN 

# # ==================================================================== #
# #                     TEMORARY PRINT OF DATA                           #
# # ==================================================================== #

print(data)

# ==================================================================== #
#                        PLOTTING THE DATA                             #
# ==================================================================== #

