# ============================================================
# UNIVERSE SELECTION AND DATA ACQUISITION
# ============================================================

import os
import time
import pandas as pd
import yfinance as yf
from datetime import date, timedelta, datetime

# ==============================
# CONFIG
# ==============================
TICKER_FILE = "data/us_tickers.txt"
UNIVERSE_FILE = "data/filtered_universe.txt"
DATA_FILE = "data/ohlcv_data.csv"

LOWEST_PRICE = 10
HIGHEST_PRICE = 50

TODAY = datetime.today().date()
NOW_TIME = datetime.now().time()

# ==============================
# DETERMINE START DATE
# ==============================
if datetime.strptime("09:00:00", "%H:%M:%S").time() < NOW_TIME:
    start_date = TODAY - timedelta(days=1)
else:
    start_date = TODAY

end_date = start_date + timedelta(days=1)

# ==============================
# UNIVERSE SELECTION
# ==============================
if not os.path.exists(UNIVERSE_FILE):
    with open(TICKER_FILE) as f:
        symbols = {line.strip().upper() for line in f if line.strip()}

    rows = []
    for symbol in symbols:
        hist = yf.Ticker(symbol).history(start=start_date, end=end_date)
        if not hist.empty:
            rows.append({
                "Symbol": symbol,
                "Close": hist["Close"].iloc[-1]
            })

    df = pd.DataFrame(rows)
    df = df[(df["Close"] > LOWEST_PRICE) & (df["Close"] < HIGHEST_PRICE)]
    df.sort_values("Close", inplace=True)

    with open(UNIVERSE_FILE, "w") as f:
        for s in df["Symbol"]:
            f.write(s + "\n")

# ==============================
# DATA DOWNLOAD
# ==============================
with open(UNIVERSE_FILE) as f:
    universe = {line.strip() for line in f if line.strip()}

all_data = []
for symbol in universe:
    data = yf.download(symbol, period="5y", interval="1d", progress=False)
    data["ticker"] = symbol
    data.reset_index(inplace=True)
    all_data.append(data)

df_all = pd.concat(all_data, ignore_index=True)
df_all.to_csv(DATA_FILE, index=False)

print("Universe selection and data download complete.")
