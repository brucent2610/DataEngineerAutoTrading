# Use an official Python runtime as a parent image
FROM python:3.11.6

RUN pip install --upgrade pip

# Set the working directory in the container to /app
WORKDIR /app

COPY . .

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt