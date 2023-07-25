from celery import Celery

app = Celery('sandp_screener')

# app.conf.broker_url = 'redis://localhost:6378'  # Redis broker
app.conf.broker_url = 'amqp://rabbitmq:rabbitmq@localhost:5672/vhost'  # RabbitMQ broker

app.conf.result_backend = 'redis://localhost:6378'

# app.autodiscover_tasks()
