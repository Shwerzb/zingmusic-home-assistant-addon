ARG BUILD_FROM=ghcr.io/hassio-addons/base:13.2.2
FROM ${BUILD_FROM}

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install Python and pip
RUN apk add --no-cache python3 py3-pip ffmpeg

# Copy source code
COPY music_assistant /app/music_assistant
COPY zingmusic_provider /app/zingmusic_provider
COPY run.sh /app/run.sh
COPY requirements.txt /app/requirements.txt

# Install Python packages
RUN pip install --no-cache-dir -r /app/requirements.txt

# Run app
RUN chmod +x /app/run.sh
CMD ["/app/run.sh"]
