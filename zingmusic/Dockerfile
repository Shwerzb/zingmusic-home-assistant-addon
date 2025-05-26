# syntax=docker/dockerfile:1
FROM ghcr.io/home-assistant/amd64-base-python:3.11-alpine

WORKDIR /app

# Install build dependencies
RUN apk add --no-cache build-base libffi-dev openssl-dev musl-dev

# Copy dependency definitions
COPY requirements_all.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements_all.txt

# Copy prebuilt wheel
COPY dist/*.whl /app/music_assistant.whl

# Install the main package
RUN pip install --no-cache-dir /app/music_assistant.whl

# Copy runtime files
COPY run.sh /app/run.sh

# Set execution permissions
RUN chmod +x /app/run.sh

# Startup command
CMD ["/app/run.sh"]
