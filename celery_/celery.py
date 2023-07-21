from celery import Celery
from celery.schedules import crontab

# app = Celery('hello', broker='amqp://guest@localhost/')
app = Celery('sandp_screener')

# app.conf.broker_url = 'redis://localhost:6379/0'
# app.conf.result_backend = 'redis://localhost:6379/0'

app.autodiscover_tasks()
