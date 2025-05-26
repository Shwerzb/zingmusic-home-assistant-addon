ARG BUILD_FROM=ghcr.io/hassio-addons/base-python:13.2.2
FROM ${BUILD_FROM}

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install runtime dependencies
RUN apk add --no-cache ffmpeg

# Copy source code
COPY music_assistant /app/music_assistant
COPY zingmusic_provider /app/zingmusic_provider
COPY run.sh /app/run.sh
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Run the app
RUN chmod +x /app/run.sh
CMD ["/app/run.sh"]
