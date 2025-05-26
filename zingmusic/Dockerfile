ARG BUILD_FROM=ghcr.io/hassio-addons/base:13.2.2
FROM ${BUILD_FROM}

ENV PYTHONUNBUFFERED=1

# ✅ Install Python 3, pip, and required build tools
RUN apk add --no-cache \
    python3 py3-pip \
    python3-dev build-base \
    libffi-dev openssl-dev \
    ffmpeg

# ✅ Set working directory
WORKDIR /app

# ✅ Copy code and install dependencies
COPY run.sh /app/run.sh
COPY requirements.txt /app/requirements.txt
COPY music_assistant /app/music_assistant
COPY zingmusic_provider /app/zingmusic_provider

# ✅ Upgrade pip/tools (only after installing pip above)
RUN pip install --upgrade pip setuptools wheel

# ✅ Install Python deps
RUN pip install --no-cache-dir -r /app/requirements.txt

# ✅ Make startup script executable
RUN chmod +x /app/run.sh

# ✅ Start the app
CMD ["/app/run.sh"]
