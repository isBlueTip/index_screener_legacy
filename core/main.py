import pandas as pd

from core.tasks import print_hello, request_cap, request_price

# STOCKS = pd.read_csv('../sp_500_stocks.csv')
STOCKS = pd.read_csv("/home/bluetip/dev/pet/sandp_screener/sp_500_stocks.csv")


def request_quotes():
    my_columns = ["Ticker", "Stock Price", "Market Capitalization", "Number of Shares to Buy"]
    final_dataframe = pd.DataFrame(columns=my_columns)

    for symbol in STOCKS["Ticker"][:3]:
        price = request_price.delay(symbol).get()
        market_cap = request_cap.delay(symbol).get() / 1000000000000

        df = pd.DataFrame(
            [
                [symbol, price, market_cap, "N/A"],
            ],
            columns=my_columns,
        )

        final_dataframe = pd.concat(
            [
                final_dataframe,
                df,
            ],
            ignore_index=True,
            axis=0,
        )
    return final_dataframe


if __name__ == "__main__":
    # app.start()
    result = request_quotes()
    # for i in range(10):
    #     result = print_hello.delay().get()
    #     print(result)

    print(f"final data = ")
    print(f"{result}")
