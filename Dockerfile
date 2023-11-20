```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /django_project

# Install system dependencies
RUN apt-get update && apt-get install -y netcat gcc

# Install python dependencies
COPY requirements.txt /django_project/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /django_project/

# Collect static files
RUN python manage.py collectstatic --noinput

# Add and run as non-root user
RUN adduser --disabled-password --gecos '' myuser
USER myuser

# Run the application:
CMD gunicorn django_project.wsgi:application --bind 0.0.0.0:$PORT
```