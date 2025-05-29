import yfinance as yf

def get_asia_tech_data():
    tickers = ['TSM', '005930.KS']  # TSMC, Samsung
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2d")
        change = (hist['Close'].iloc[-1] - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2] * 100
        data[ticker] = {'latest': hist['Close'].iloc[-1], 'change_%': round(change, 2)}
    return data
    