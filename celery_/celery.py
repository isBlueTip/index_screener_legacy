from celery import Celery

app = Celery("sandp_screener")

# app.conf.broker_url = 'redis://localhost:6378'  # Redis broker
app.conf.broker_url = "amqp://rabbitmq:rabbitmq@localhost:5672/vhost"  # RabbitMQ broker
# app.conf.broker_url = "amqp://guest:guest@localhost:5672//"  # RabbitMQ broker

app.conf.result_backend = "redis://localhost:6379"

# app.autodiscover_tasks()


flower_app = Celery("flower_app")

# flower_app.conf.broker_url = "amqp://guest:guest@localhost:5672//"  # flower broker
flower_app.conf.broker_url = "amqp://rabbitmq:rabbitmq@localhost:5672/vhost"  # flower broker
