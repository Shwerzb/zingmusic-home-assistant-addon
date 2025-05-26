ARG BUILD_FROM=ghcr.io/hassio-addons/base:13.2.2
FROM ${BUILD_FROM}

ENV PYTHONUNBUFFERED=1

# ✅ Install Python and all required tools
RUN apk add --no-cache \
    python3 py3-pip \
    python3-dev build-base \
    libffi-dev openssl-dev ffmpeg

# ✅ Set working directory
WORKDIR /app

# ✅ Copy everything
COPY run.sh /app/run.sh
COPY requirements.txt /app/requirements.txt
COPY music_assistant /app/music_assistant
COPY zingmusic_provider /app/zingmusic_provider

# ✅ Upgrade pip, setuptools, wheel
RUN pip install --upgrade pip setuptools wheel

# ✅ Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# ✅ Make the script executable and run
RUN chmod +x /app/run.sh
CMD ["/app/run.sh"]
