import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from scipy import stats

# 2. The Avarage stratagies
def analyze_stock(symbol, stock_data):
    history = stock_data['history']
    info = stock_data['info']

    # Calculate returns
    current_price = history['Close'].iloc[-1] if not history.empty else None
    one_month_ago = datetime.now() - timedelta(days=30)
    six_months_ago = datetime.now() - timedelta(days=180)
    one_year_ago = datetime.now() - timedelta(days=365)

    month_history = history[history.index >= one_month_ago]
    six_month_history = history[history.index >= six_months_ago]
    year_history = history[history.index >= one_year_ago]

    one_month_return = ((current_price / month_history['Close'].iloc[0] - 1) * 100) if not month_history.empty else None
    six_month_return = ((current_price / six_month_history['Close'].iloc[0] - 1) * 100) if not six_month_history.empty else None
    one_year_return = ((current_price / year_history['Close'].iloc[0] - 1) * 100) if not year_history.empty else None

    # Calculate volatility
    daily_returns = history['Close'].pct_change()
    volatility = daily_returns.std() * np.sqrt(252)  # Annualized volatility

    # Extract key financials and ratios
    market_cap = info.get('marketCap')
    pe_ratio = info.get('trailingPE')
    forward_pe = info.get('forwardPE')
    peg_ratio = info.get('pegRatio')
    price_to_book = info.get('priceToBook')
    dividend_yield = info.get('dividendYield', 0) * 100
    debt_to_equity = info.get('debtToEquity')
    return_on_equity = info.get('returnOnEquity')
    profit_margin = info.get('profitMargins')
    beta = info.get('beta')

    return {
        'symbol': symbol,
        'name': info.get('longName', symbol),  # Use longName if available, otherwise use symbol
        'current_price': current_price,
        'one_month_return': one_month_return,
        'six_month_return': six_month_return,
        'one_year_return': one_year_return,
        'volatility': volatility,
        'market_cap': market_cap,
        'pe_ratio': pe_ratio,
        'forward_pe': forward_pe,
        'peg_ratio': peg_ratio,
        'price_to_book': price_to_book,
        'dividend_yield': dividend_yield,
        'debt_to_equity': debt_to_equity,
        'return_on_equity': return_on_equity,
        'profit_margin': profit_margin,
        'beta': beta
    }
