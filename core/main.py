import pandas as pd

from celery_.celery import app, flower_app
from core.tasks import print_hello, request_cap, request_price

# STOCKS = pd.read_csv('../sp_500_stocks.csv')
STOCKS = pd.read_csv("/home/bluetip/dev/pet/sandp_screener/sp_500_stocks.csv")


def request_quotes(source: str) -> type(pd.DataFrame):
    my_columns = ["Ticker", "Stock Price", "Market Capitalization", "Number of Shares to Buy"]
    final_dataframe = pd.DataFrame(columns=my_columns)

    for symbol in STOCKS["Ticker"][:10]:
        if source == "alpha":
            price = request_price.delay(symbol).get()
            market_cap = request_cap.delay(symbol).get()
        elif source == "finnhub":
            price = request_price.delay(symbol).get()
            market_cap = request_cap.delay(symbol).get()

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


def build_xlsx(filename: str, dataframe: type(pd.DataFrame)):
    writer = pd.ExcelWriter(f"{filename}.xlsx", engine="xlsxwriter")
    dataframe.to_excel(writer, "Recommended trades", index=False)

    background_color = "#0a0a23"
    font_color = "#ffffff"

    string_format = writer.book.add_format(
        {
            "font_color": font_color,
            "bg_color": background_color,
            "border": 1,
        }
    )
    dollar_format = writer.book.add_format(
        {
            "num_format": "$0.00",
            "font_color": font_color,
            "bg_color": background_color,
            "border": 1,
        }
    )
    integer_format = writer.book.add_format(
        {
            "num_format": "0",
            "font_color": font_color,
            "bg_color": background_color,
            "border": 1,
        }
    )

    column_formats = {
        "A": ["Ticker", string_format, 10],
        "B": ["Price", dollar_format, 15],
        "C": ["Market Capitalization", dollar_format, 20],
        "D": ["Number of Shares to Buy", integer_format, 25],
    }

    for column in column_formats.keys():
        writer.sheets["Recommended trades"].set_column(
            f"{column}:{column}", column_formats[column][2], column_formats[column][1]
        )
        writer.sheets["Recommended trades"].write(f"{column}1", column_formats[column][0], string_format)

    writer.close()


if __name__ == "__main__":
    # app.start()
    result = request_quotes("finnhub")
    # for i in range(10):
    #     result = print_hello.delay().get()
    #     print(result)

    build_xlsx("recommended trades", result)

    print(f"final data = ")
    print(f"{result}")
