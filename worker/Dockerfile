# Use the official Python 3.9 image as a parent image
FROM python:3.11-slim

# Set the working directory in the container to /usr/src/app
WORKDIR /usr/src/app

# Copy the requirements file from the root context and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the worker directory into the container
COPY ./worker .
# Copy the common directory into the container
COPY ./common /usr/src/app/common
ENV PYTHONPATH=/usr/src/app
# Run the Celery worker on container startup
CMD ["celery", "-A", "tasks", "worker", "--loglevel=info", "--concurrency=4"]
