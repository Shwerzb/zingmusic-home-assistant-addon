# syntax=docker/dockerfile:1

ARG BASE_IMAGE_VERSION=latest
FROM ghcr.io/music-assistant/base:$BASE_IMAGE_VERSION AS builder

WORKDIR /app

# Install base Python packaging tools
RUN pip install --upgrade pip setuptools wheel

# Copy your built wheel and requirements
COPY dist/*.whl /app/music_assistant.whl
COPY requirements_all.txt .

# Install requirements and your app's wheel
RUN pip install --no-cache-dir -r requirements_all.txt && \
    pip install --no-cache-dir /app/music_assistant.whl

# Set correct permissions
RUN chmod -R 777 /app

####################################################################

# Final image
FROM ghcr.io/music-assistant/base:$BASE_IMAGE_VERSION

WORKDIR /app

# Copy all from builder
COPY --from=builder /app /app

# Add and allow run.sh
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

ENV PATH="/app/venv/bin:$PATH"

VOLUME ["/data"]
EXPOSE 8095

CMD ["/app/run.sh"]
