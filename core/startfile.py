import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

from utils.urls import get_quote_url, get_company_overview_url

stocks = pd.read_csv('sp_500_stocks.csv')

# symbol = 'AAPL'
# quote_url = get_quote_url(symbol)
# company_overview_url = get_company_overview_url(symbol)
#
# data_price = requests.get(quote_url).json()
# data_cap = requests.get(company_overview_url).json()
#
# price = float(data_price.get('Global Quote').get('05. price'))
# market_cap = float(data_cap.get('MarketCapitalization'))
# print(f"price = {price}")
# print(f"market_cap = {market_cap/1000000000000}")

my_columns = ['Ticker', 'Stock Price', 'Market Capitalization', 'Number of Shares to Buy']
final_dataframe = pd.DataFrame(columns=my_columns)


for symbol in stocks['Ticker'][:5]:
    quote_url = get_quote_url(symbol)
    company_overview_url = get_company_overview_url(symbol)

    data_price = requests.get(quote_url).json()
    data_cap = requests.get(company_overview_url).json()

    price = float(data_price.get('Global Quote').get('05. price'))
    market_cap = float(data_cap.get('MarketCapitalization'))

    pd.concat(
        [
            final_dataframe,
            pd.DataFrame(
                [
                    [
                        symbol,
                        price,
                        market_cap,
                        'N/A'
                    ],
                ],
                columns=my_columns
            )
        ]
    )
else:
    print(final_dataframe)

#
# symbols = 'aapl,fb,ba'
# quote_url = f'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols={symbols}&apikey={ALPHA_VANTAGE_API_TOKEN}'
#
# response = requests.get(quote_url).json()
# print(response)