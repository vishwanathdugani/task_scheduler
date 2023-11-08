# Task Scheduler Project

## Overview
This Task Scheduler is a distributed computing project which utilizes Celery with RabbitMQ as a message broker to distribute tasks across multiple workers. It includes an API to submit tasks and a client to enqueue them. The project demonstrates the fundamental concepts of distributed task queues using simple arithmetic operations and string manipulation.

## Getting Started

### Prerequisites
- Docker
- Docker Compose
- Git
- Python 3.11 or higher

### Setup Instructions

1. Clone the repository:
   ```sh
   git clone https://github.com/vishwanathdugani/task_scheduler.git
   ```

2. Navigate to the project directory:
   ```sh
   cd task_scheduler
   ```

3. Build the Docker images and start the services using Docker Compose:
   ```sh
   docker-compose up --build -d
   ```

### Distributed Computing with Workers

The system is designed to run four worker services in parallel, allowing for distributed processing of tasks. Each worker listens to a queue and processes tasks independently. This improves the throughput and resilience of the application, as tasks are distributed and processed concurrently.

### API Documentation

The API documentation is available at [http://localhost:8000/docs#](http://localhost:8000/docs#) where you can interact with the API and post tasks.

### Client Script

After building the Docker images and running the services, execute the `client.py` script to post tasks to the queue:
```sh
python client/client.py
```

### Task Types

Tasks that can be submitted include:
- Addition (`add`)
- Multiplication (`multiply`)
- String Uppercase Conversion (`upper_case`)

These tasks are meant for demonstration and showcase how tasks are distributed and processed by the workers.

### Future Improvements

Please note that this implementation was done with limited time, and more improvements will follow soon.
- **Dynamic Scaling:** Implement functionality to add or remove workers based on the current load.
- **Testing:** Increase the coverage and scope of automated tests.
- **Logging:** Enhance logging mechanisms for better tracking and debugging.
- **Optimization:** Fine-tune the worker handling for more efficient processing.
- **Security:** Securing APIs and message broker for unauthorized entries.
- **UI:** A UI to login and add tasks to process

## API Endpoints

The API provides the following endpoints:

- `POST /add`: Enqueues an addition task.
- `POST /multiply`: Enqueues a multiplication task.
- `POST /upper_case`: Enqueues a task to convert a string to uppercase.
- `GET /status/{task_id}`: Retrieves the status and result of a task by its ID.

## Task Definitions

Each task is defined in the `tasks` module and is equipped with automatic retry capabilities on failure, up to a maximum of five retries with exponential backoff.
