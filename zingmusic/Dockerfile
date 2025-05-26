# syntax=docker/dockerfile:1

ARG BASE_IMAGE_VERSION=latest
FROM ghcr.io/music-assistant/base:$BASE_IMAGE_VERSION AS builder

WORKDIR /app

# Add your prebuilt wheel
ADD dist dist

# Ensure UV is available for fast pip installs
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create virtual environment
ENV VIRTUAL_ENV=/app/venv
RUN uv venv $VIRTUAL_ENV

# Install your ZingMusic-enabled Music Assistant wheel
RUN uv pip install \
    --find-links "https://wheels.home-assistant.io/musllinux/" \
    dist/music_assistant-*.whl

# Set full permissions for HA Supervisor compatibility
RUN chmod -R 777 /app

# === Final runtime container ===
FROM ghcr.io/music-assistant/base:$BASE_IMAGE_VERSION

ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy everything from builder
COPY --from=builder /app /app

# Copy startup script and fix permissions
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh && dos2unix /app/run.sh || true

WORKDIR /app

LABEL \
    io.hass.name="ZingMusic" \
    io.hass.description="ZingMusic Add-on for Music Assistant" \
    io.hass.version="1.0.0" \
    io.hass.type="addon"

VOLUME [ "/data" ]
EXPOSE 8095

CMD [ "/app/run.sh" ]
