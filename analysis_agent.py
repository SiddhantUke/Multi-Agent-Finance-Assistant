def analyze_risk(market_data):
    asia_exposure = (market_data['TSM']['latest'] + market_data['005930.KS']['latest']) * 1000
    return f"Asia Tech Exposure: {asia_exposure:.2f} USD"