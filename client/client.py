import time
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_URL = "http://localhost:8000"


def submit_task(endpoint: str, payload: dict) -> dict:
    """
    Submit a task to the API and return the response.

    Args:
        endpoint (str): The API endpoint for task submission.
        payload (dict): The data payload for the task.

    Returns:
        dict: The JSON response from the API.
    """
    response = requests.post(f"{API_URL}/{endpoint}", json=payload)
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        logger.error(f"Failed to decode JSON from response: {response.text}", exc_info=True)
        response.raise_for_status()


def get_task_status(celery_task_id: str) -> dict:
    """
    Get the status of a task from the API using the task ID.

    Args:
        celery_task_id (str): The ID of the Celery task.

    Returns:
        dict: The JSON response with the task status.
    """
    response = requests.get(f"{API_URL}/status/{celery_task_id}")
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        logger.error(f"Failed to decode JSON from response: {response.text}", exc_info=True)
        response.raise_for_status()


def main():
    """
    Main function to submit tasks and check their statuses.
    """
    task_ids = []

    for i in range(50):
        add_task = submit_task("add", {"x": i, "y": i + 1})
        logger.info(f"Add Task {i + 1} submitted, ID: {add_task['task_id']}")
        task_ids.append(add_task['task_id'])

        multiply_task = submit_task("multiply", {"x": i, "y": i + 2})
        logger.info(f"Multiply Task {i + 1} submitted, ID: {multiply_task['task_id']}")
        task_ids.append(multiply_task['task_id'])

        upper_case_task = submit_task("upper_case", {"text": f"string {i}"})
        logger.info(f"UpperCase Task {i + 1} submitted, ID: {upper_case_task['task_id']}")
        task_ids.append(upper_case_task['task_id'])

    for task_id in task_ids:
        status = None
        while status != "SUCCESS":
            status_response = get_task_status(task_id)
            status = status_response['status']
            result = status_response.get('result', None)
            logger.info(f"Task ID: {task_id}, Status: {status}, Result: {result}")
            if status != "SUCCESS":
                time.sleep(1)


if __name__ == "__main__":
    main()
