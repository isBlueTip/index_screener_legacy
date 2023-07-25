from celery import Celery, shared_task

from celery_.celery import app


@shared_task
# @app.task
def hello():
    return "hello world"
