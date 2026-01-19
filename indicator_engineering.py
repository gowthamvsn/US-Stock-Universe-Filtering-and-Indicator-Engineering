# ============================================================
# TECHNICAL INDICATOR ENGINEERING
# ============================================================

import pandas as pd
import stockstats

DATA_FILE = "data/ohlcv_data.csv"
OUTPUT_FILE = "data/indicator_data.csv"

df = pd.read_csv(DATA_FILE, parse_dates=["Date"])

frames = []
for ticker in df["ticker"].unique():
    subset = df[df["ticker"] == ticker]
    stock = stockstats.StockDataFrame.retype(subset)

    stock["close_14_sma"]
    stock["boll"]
    stock["boll_ub"]
    stock["boll_lb"]
    stock["stochrsi_14"]
    stock["rsi_14"]
    stock["vwma_14"]
    stock["atr_14"]
    stock["kdjk_14"]
    stock["kdjd_14"]
    stock["kdjj_14"]
    stock["trix_14"]
    stock["macd"]
    stock["macds"]
    stock["macdh"]
    stock["close_14_roc"]
    stock["cci_14"]

    frames.append(stock)

final_df = pd.concat(frames, ignore_index=True)
final_df.to_csv(OUTPUT_FILE, index=False)

print("Indicator engineering complete.")
