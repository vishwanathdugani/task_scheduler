import sys
from typing import Any
from celery import Task
from celery.utils.log import get_task_logger
from common.celery_app import celery_app

# Configure the logger
logger = get_task_logger(__name__)

# Extend the Python path to include the common directory
sys.path.append('/usr/src/common')

class RetryableTask(Task):
    """
    A Celery Task class that is set to automatically retry on failure.

    Attributes:
        autoretry_for: A tuple of exception classes that should trigger a retry.
        retry_kwargs: A dictionary that defines max_retries and other retry settings.
        retry_backoff: Boolean that enables or disables exponential backoff.
    """
    autoretry_for = (Exception,)
    retry_kwargs = {'max_retries': 5}
    retry_backoff = True


@celery_app.task(bind=True, base=RetryableTask)
def add(self: Task, x: int, y: int) -> int:
    """
    Add two integers together.

    Args:
        self (Task): The Celery task instance.
        x (int): First integer to add.
        y (int): Second integer to add.

    Returns:
        int: The result of adding x and y.
    """
    logger.info(f"Adding {x} + {y}")
    return x + y


@celery_app.task(bind=True, base=RetryableTask)
def multiply(self: Task, x: int, y: int) -> int:
    """
    Multiply two integers.

    Args:
        self (Task): The Celery task instance.
        x (int): First integer to multiply.
        y (int): Second integer to multiply.

    Returns:
        int: The result of multiplying x and y.
    """
    logger.info(f"Multiplying {x} * {y}")
    return x * y


@celery_app.task(bind=True, base=RetryableTask)
def upper_case(self: Task, text: str) -> str:
    """
    Convert a string to uppercase.

    Args:
        self (Task): The Celery task instance.
        text (str): The string to convert.

    Returns:
        str: The uppercase version of the input text.
    """
    logger.info(f"Uppercasing '{text}'")
    return text.upper()
