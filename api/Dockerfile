# Use the official Python 3.9 image as a parent image
FROM python:3.11-slim

# Set the working directory in the container to /usr/src/app
WORKDIR /usr/src/app

# Copy the requirements file from the root context and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the api directory into the container
COPY ./api .
# Copy the common directory into the container
COPY ./common /usr/src/app/common

# Command to run the uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
