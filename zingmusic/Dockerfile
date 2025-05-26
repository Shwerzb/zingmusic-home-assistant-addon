ARG BUILD_FROM=ghcr.io/hassio-addons/base-python:13.2.2
FROM ${BUILD_FROM}

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
    python3-dev build-base libffi-dev openssl-dev ffmpeg

WORKDIR /app

COPY run.sh /app/run.sh
COPY requirements.txt /app/requirements.txt
COPY music_assistant /app/music_assistant
COPY zingmusic_provider /app/zingmusic_provider

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r /app/requirements.txt

RUN chmod +x /app/run.sh
CMD ["/app/run.sh"]
