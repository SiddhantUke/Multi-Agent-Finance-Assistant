from agents.api_agent import get_asia_tech_data
from agents.scraping_agent import scrape_earnings_news
from agents.retriever_agent import build_index, retrieve
from agents.analysis_agent import analyze_risk
from agents.language_agent import generate_response

def run_pipeline(query):
    market_data = get_asia_tech_data()
    headlines = scrape_earnings_news()
    risk_report = analyze_risk(market_data)

    context = f"{headlines}\n{risk_report}\n{market_data}"
    build_index([context])
    top_chunks = retrieve(query)

    return generate_response(query, "\n".join(top_chunks))