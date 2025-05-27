# ===================================================================== #
#                         IMPORTING MODULES                             #
# ===================================================================== #
import os
import time
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from rich import print as rprint
from rich.panel import Panel
from rich.progress import track

# ===================================================================== #
#                          GLOBAL CONFIGS                               #
# ===================================================================== #
RETRIES = 3
SHORT_WINDOW = 5
LONG_WINDOW = 20

# ===================================================================== #
#                          LOAD TICKER DATA                             #
# ===================================================================== #
ticker_list = pd.read_csv("tickers.csv")
rprint(f"[#DFF2F8]{ticker_list}")

# ===================================================================== #
#                       USER SELECTS A COMPANY                          #
# ===================================================================== #
try:
    ticker_index = int(input("Enter a number (0–9) to select a company: "))
    if not (0 <= ticker_index < len(ticker_list)):
        raise ValueError("Invalid input! Please enter a number between 0 and 9.")
    print("You selected:", ticker_index)
except ValueError as e:
    rprint(f"[bold red]ERROR: {e}")
    exit()

# ===================================================================== #
#                         DOWNLOAD STOCK DATA                           #
# ===================================================================== #
ticker = ticker_list['Ticker'][ticker_index]
company_name = ticker_list['Company Name'][ticker_index]

for attempt in range(1, RETRIES + 1):
    try:
        rprint(f"[bold yellow][ATTEMPT {attempt}] Downloading data for {company_name}")
        data = yf.download(ticker, period="6mo")

        for _ in track(range(10), description="LOADING DATA..."):
            time.sleep(0.2)

        if data.empty:
            raise ValueError(f"No data found for ticker: {company_name}")

        rprint(f"[bold green]SUCCESS: Data for {company_name} loaded.")
        break

    except ValueError as ve:
        rprint(f"[bold red]{ve}")
        exit()
    except Exception as e:
        rprint(f"[bold red]Error downloading {company_name}: {e}")
        if attempt < RETRIES:
            rprint("[bold yellow]Retrying...")
            time.sleep(1.5)
        else:
            rprint("[bold red]Failed after multiple attempts.")
            exit()

# =================================================================== #
#                  CALCULATE SMA CROSSOVER                            #
# =================================================================== #
sma_data = pd.DataFrame(index=data.index)
sma_data['SMAshort'] = data['Close'].rolling(window=SHORT_WINDOW).mean()
sma_data['SMAlong'] = data['Close'].rolling(window=LONG_WINDOW).mean()

sma_data['Signalbuy'] = (
    (sma_data['SMAshort'] > sma_data['SMAlong']) &
    (sma_data['SMAshort'].shift(1) < sma_data['SMAlong'].shift(1))
)

sma_data['Signalsell'] = (
    (sma_data['SMAshort'] < sma_data['SMAlong']) &
    (sma_data['SMAshort'].shift(1) > sma_data['SMAlong'].shift(1))
)

# ================================================================== #
#                        DISPLAYING SUMMARY                          #
# ================================================================== #
latest = sma_data.dropna().iloc[-1]
last_close = data['Close'].iloc[-1].item()
status = "[extrabold green]BUY" if latest['SMAshort'] > latest['SMAlong'] else "[extrabold red]SELL"

message = f"""
[bold]{ticker}[/bold]
[cyan]Latest Close:[/] ${last_close:.2f}
[cyan]{SHORT_WINDOW}-Day SMA:[/] ${latest['SMAshort']:.2f}
[cyan]{LONG_WINDOW}-Day SMA:[/] ${latest['SMAlong']:.2f}

[bold]{status} signal based on SMA crossover[/bold]
"""

panel = Panel(message, title="SMA Crossover Summary", border_style="bright_blue")
print(panel)
rprint(panel)

# ================================================================= #
#                            PLOT THE GRAPH                         #
# ================================================================= #
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Close'], label='Close Price', color='blue', alpha=0.6)
plt.plot(sma_data.index, sma_data['SMAshort'], label=f'{SHORT_WINDOW}-Day SMA', color='orange')
plt.plot(sma_data.index, sma_data['SMAlong'], label=f'{LONG_WINDOW}-Day SMA', color='magenta')

# Buy signals
plt.scatter(
    sma_data.index[sma_data['Signalbuy']],
    data['Close'][sma_data['Signalbuy']],
    label='Buy Signal',
    marker='^',
    color='green',
    s=100
)

# Sell signals
plt.scatter(
    sma_data.index[sma_data['Signalsell']],
    data['Close'][sma_data['Signalsell']],
    label='Sell Signal',
    marker='v',
    color='red',
    s=100
)

plt.title(f'{ticker} Price & SMA Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
