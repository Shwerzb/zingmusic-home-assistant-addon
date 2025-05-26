# Use an official Python base image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install build tools and runtime dependencies
RUN apk add --no-cache \
    bash \
    git \
    ffmpeg \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    py3-pip \
    py3-setuptools \
    py3-wheel \
    tzdata \
    py3-cryptography \
    libxml2-dev \
    libxslt-dev \
    py3-lxml \
    py3-cffi

# Create workdir
WORKDIR /app

# Copy the full Music Assistant source
COPY ./music_assistant /app/music_assistant

# Copy the custom ZingMusic provider to the providers folder
COPY ./zingmusic_provider /app/music_assistant/providers/zingmusic

# Copy entrypoint script
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# Install Music Assistant server dependencies from the local source
COPY requirements_all.txt /app/requirements_all.txt
RUN pip install -r /app/requirements_all.txt

# Final entrypoint
CMD ["/app/run.sh"]
