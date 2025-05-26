# syntax=docker/dockerfile:1

ARG BASE_IMAGE_VERSION=latest
FROM ghcr.io/music-assistant/base:$BASE_IMAGE_VERSION AS builder

# Workdir for wheel install
WORKDIR /app

# Copy wheel and requirements
COPY dist/*.whl /app/music_assistant.whl
COPY requirements_all.txt .

# Install dependencies using uv (already in base image)
RUN uv pip install \
    --find-links "https://wheels.home-assistant.io/musllinux/" \
    -r requirements_all.txt && \
    uv pip install \
    --no-cache \
    --find-links "https://wheels.home-assistant.io/musllinux/" \
    /app/music_assistant.whl

RUN chmod -R 777 /app

#####################################################################

# Final image
FROM ghcr.io/music-assistant/base:$BASE_IMAGE_VERSION

WORKDIR /app

# Copy full /app including venv
COPY --from=builder /app /app

# Add and allow run.sh
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

ENV PATH="/app/venv/bin:$PATH"

# Set labels
LABEL \
    org.opencontainers.image.title="ZingMusic Add-on" \
    org.opencontainers.image.description="Music Assistant with ZingMusic provider" \
    org.opencontainers.image.source="https://github.com/Shwerzb/zingmusic-home-assistant-addon"

VOLUME ["/data"]
EXPOSE 8095

CMD ["/app/run.sh"]
