import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import time

#its make alot of api call so it take alittle time Do not Run this function twice its pirpise is to store all the stocks details in memory
class StockDataCache:
    def __init__(self):
        self.cache = {}

    def fetch_and_store_data(self, symbols, days=365):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        for symbol in symbols:
            if symbol not in self.cache:
                try:
                    stock = yf.Ticker(symbol)
                    history = stock.history(start=start_date, end=end_date)
                    info = stock.info
                    self.cache[symbol] = {
                        'history': history,
                        'info': info
                    }
                    #print(f"\rFetching data: {symbol}", end="", flush=True)
                    # Create a progress bar animation
                    progress = (symbols.index(symbol) + 1) / len(symbols)
                    bar_length = 20
                    filled_length = int(bar_length * progress)
                    bar = '█' * filled_length + '-' * (bar_length - filled_length)
                    percent = progress * 100
                    print(f"\rProgress: |{bar}| {percent:.1f}% Complete", end="", flush=True)
                    time.sleep(0.1)  # Small delay to make the progress visible

                except Exception as e:
                    print(f"Error fetching data for {symbol}: {e}")
            else:
                print(f"Data for {symbol} already in cache")

    def get_stock_data(self, symbol):
        return self.cache.get(symbol)

    def get_all_symbols(self):
        return list(self.cache.keys())

# Function to initialize and populate the cache
def initialize_stock_cache():
    cache = StockDataCache()
    symbols = get_nifty500_symbols()
    cache.fetch_and_store_data(symbols)
    return cache
