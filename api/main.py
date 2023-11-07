from fastapi import FastAPI
from schemas import AddInput, MultiplyInput, UpperCaseInput
from common.celery_app import celery_app
from fastapi.responses import JSONResponse
import logging


# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.post("/add")
def enqueue_add_task(task_input: AddInput) -> JSONResponse:
    """
    Enqueue an addition task.

    Args:
        task_input (AddInput): The input containing two integers to be added.

    Returns:
        JSONResponse: A JSON response with the task ID.
    """
    task = celery_app.send_task('tasks.add', args=[task_input.x, task_input.y])
    logger.info(f"Add task enqueued with ID: {task.id}")
    return JSONResponse({"task_id": task.id})


@app.post("/multiply")
def enqueue_multiply_task(task_input: MultiplyInput) -> JSONResponse:
    """
    Enqueue a multiplication task.

    Args:
        task_input (MultiplyInput): The input containing two integers to be multiplied.

    Returns:
        JSONResponse: A JSON response with the task ID.
    """
    task = celery_app.send_task('tasks.multiply', args=[task_input.x, task_input.y])
    logger.info(f"Multiply task enqueued with ID: {task.id}")
    return JSONResponse({"task_id": task.id})


@app.post("/upper_case")
def enqueue_upper_case_task(task_input: UpperCaseInput) -> JSONResponse:
    """
    Enqueue a task to convert a string to upper case.

    Args:
        task_input (UpperCaseInput): The input containing a string to be converted to upper case.

    Returns:
        JSONResponse: A JSON response with the task ID.
    """
    task = celery_app.send_task('tasks.upper_case', args=[task_input.text])
    logger.info(f"Upper case task enqueued with ID: {task.id}")
    return JSONResponse({"task_id": task.id})


@app.get("/status/{task_id}")
def get_task_status(task_id: str) -> JSONResponse:
    """
    Get the status of a task given its ID.

    Args:
        task_id (str): The task ID to query.

    Returns:
        JSONResponse: A JSON response with the task ID, status, and result.
    """
    task_result = celery_app.AsyncResult(task_id)
    status = task_result.status
    result = task_result.result if task_result.result else None
    response = {
        "task_id": task_id,
        "status": status,
        "result": result,
    }
    logger.info(f"Task status queried for ID: {task_id} - Status: {status}")
    return JSONResponse(response)
