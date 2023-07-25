from celery import Celery, shared_task
from celery_.celery import app
from utils.urls import get_quote_url, get_company_overview_url
import requests


# @app.on_after_configure
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(5.0, hello.s('hello'), name='add every 10')
#
#     # Calls test('hello') every 30 seconds.
#     # It uses the same signature of previous task, an explicit name is
#     # defined to avoid this task replacing the previous one defined.
#     # sender.add_periodic_task(30.0, test.s('hello'), name='add every 30')

@app.task(rate_limit='10/m')
def print_hello() -> str:
    return 'hello world'


@app.task(rate_limit='2/m')
def request_price(symbol: str) -> float:
    quote_url = get_quote_url(symbol)

    data_price = requests.get(quote_url).json()

    print(f'price data = {data_price}')
    print(f'\n')

    price = float(data_price.get('Global Quote').get('05. price'))

    return price


@app.task(rate_limit='2/m')
def request_cap(symbol: str) -> float:
    company_overview_url = get_company_overview_url(symbol)

    data_cap = requests.get(company_overview_url).json()
    print(f'cap data = {data_cap}')
    print(f'\n')

    market_cap = float(data_cap.get('MarketCapitalization'))

    return market_cap
