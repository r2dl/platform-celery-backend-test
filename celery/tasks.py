import os
import time
from celery import Celery
from main_service.main_service_functions import (
    get_results,
    delete_results,
    post_results,
)


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="create_task")
def create_task(task_data):
    payload = post_results(task_data)
    return payload

