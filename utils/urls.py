from secrets_ import ALPHA_VANTAGE_API_TOKEN


def get_quote_url(symbol: str) -> str:
    # quote_url
    return f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={ALPHA_VANTAGE_API_TOKEN}'


def get_company_overview_url(symbol: str) -> str:
    # company_overview_url
    return f'https://www.alphavantage.co/query?function=overview&symbol={symbol}&apikey={ALPHA_VANTAGE_API_TOKEN}'
