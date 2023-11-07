from celery import Celery
from common import celery_config


# Initialize Celery app
celery_app = Celery('distributed_task_scheduler')

# Load configuration from a configuration object
celery_app.config_from_object(celery_config)

# Ensure the worker will import the tasks module upon starting
celery_app.autodiscover_tasks(lambda: celery_app.conf.imports)

