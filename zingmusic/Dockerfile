ARG BUILD_FROM=ghcr.io/hassio-addons/base:13.2.2
FROM ${BUILD_FROM}

ENV PYTHONUNBUFFERED=1

# Install Python + Pip + build deps
RUN apk add --no-cache \
    python3 py3-pip \
    python3-dev build-base \
    libffi-dev openssl-dev \
    ffmpeg

WORKDIR /app

# Copy files
COPY music_assistant /app/music_assistant
COPY zingmusic_provider /app/zingmusic_provider
COPY requirements.txt /app/requirements.txt
COPY run.sh /app/run.sh

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Final setup
RUN chmod +x /app/run.sh
CMD ["/app/run.sh"]
