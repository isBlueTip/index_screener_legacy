from celery import Celery, shared_task
from celery_.celery import app
from utils.urls import get_quote_url, get_company_overview_url
import requests
import pandas as pd


# @app.on_after_configure
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(5.0, hello.s('hello'), name='add every 10')
#
#     # Calls test('hello') every 30 seconds.
#     # It uses the same signature of previous task, an explicit name is
#     # defined to avoid this task replacing the previous one defined.
#     # sender.add_periodic_task(30.0, test.s('hello'), name='add every 30')


@shared_task
# @app.task
def print_hello() -> str:
    return 'hello world'


# @shared_task
@app.task(rate_limit=10)
def request_quote(symbol: str) -> (float, float):

    quote_url = get_quote_url(symbol)
    company_overview_url = get_company_overview_url(symbol)

    data_price = requests.get(quote_url).json()
    data_cap = requests.get(company_overview_url).json()

    price = float(data_price.get('Global Quote').get('05. price'))
    market_cap = float(data_cap.get('MarketCapitalization'))

    return price, market_cap
