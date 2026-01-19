# US Stock Universe Filtering and Indicator Engineering

This project builds a data pipeline for selecting a tradable universe
of US equities and computing a broad set of technical indicators
for downstream analysis or modeling.

The focus is on **data preparation**, not prediction.

---

## Why This Project?

Most trading and ML projects skip an important step:
**how the stock universe and features are constructed**.

This project addresses that gap by:
- Filtering stocks based on price constraints
- Maintaining a reusable stock universe
- Downloading historical OHLCV data
- Computing a wide range of technical indicators
- Producing clean, indicator-rich datasets

These outputs can later be used for:
- Strategy research
- Feature selection
- Signal evaluation
- Machine learning models

---

## Data Sources

- **Market Data**: Yahoo Finance (yfinance)
- **Indicators**: stockstats
- **Universe**: US equity ticker lists

---

## Pipeline Overview

### Stage 1: Universe Selection
- Filter US stocks by price range
- Persist selected tickers
- Avoid repeated filtering on subsequent runs

### Stage 2: Data Acquisition
- Download multi-year OHLCV data
- Incrementally update stored datasets

### Stage 3: Indicator Engineering
- Compute trend, momentum, volatility indicators
- Store enriched datasets for reuse

---

## Indicators Computed

- SMA, VWMA
- RSI, Stochastic RSI
- Bollinger Bands
- ATR, TRIX
- MACD (line, signal, histogram)
- ROC, CCI
- DMA and deviation measures

---

## File Structure
```
src/
├── universe_selection.py
├── indicator_engineering.py
```
## Author
Gowtham Vuppaladhadiam


