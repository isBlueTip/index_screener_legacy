import pandas as pd

from celery_.celery import app
from celery_.tasks import hello
from core.tasks import request_cap, request_price

# STOCKS = pd.read_csv('../sp_500_stocks.csv')
STOCKS = pd.read_csv("/home/bluetip/dev/pet/sandp_screener/sp_500_stocks.csv")


def request_quotes():
    my_columns = ["Ticker", "Stock Price", "Market Capitalization", "Number of Shares to Buy"]
    final_dataframe = pd.DataFrame(columns=my_columns)

    for symbol in STOCKS["Ticker"][:1]:
        price = request_price.delay(symbol).get()
        market_cap = request_cap.delay(symbol).get()

        print(f"price = {price}")
        print(f"market_cap = {market_cap / 1000000000000}")

        final_dataframe += pd.concat(
            [
                final_dataframe,
                pd.DataFrame(
                    [
                        [symbol, price, market_cap, "N/A"],
                    ],
                    columns=my_columns,
                ),
            ]
        )
        print(f"final_dataframe = {final_dataframe}")
    print(final_dataframe)


if __name__ == "__main__":
    # app.start()
    request_quotes()
