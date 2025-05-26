# syntax=docker/dockerfile:1

ARG BASE_IMAGE_VERSION=latest
FROM ghcr.io/music-assistant/base:$BASE_IMAGE_VERSION AS builder

# Add your wheel + requirements
ADD dist dist
COPY requirements_all.txt .

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create venv
ENV VIRTUAL_ENV=/app/venv
RUN uv venv $VIRTUAL_ENV

# Install requirements into venv
RUN uv pip install \
    --find-links "https://wheels.home-assistant.io/musllinux/" \
    -r requirements_all.txt

# Install your custom Music Assistant wheel (with ZingMusic integrated)
ARG MASS_VERSION
RUN uv pip install \
    --no-cache \
    --find-links "https://wheels.home-assistant.io/musllinux/" \
    "music-assistant@dist/music_assistant-${MASS_VERSION}-py3-none-any.whl"

# Set permissions
RUN chmod -R 777 /app

# FINAL STAGE
FROM ghcr.io/music-assistant/base:$BASE_IMAGE_VERSION

ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --from=builder /app /app
RUN chmod 777 /app

ARG MASS_VERSION
ARG TARGETPLATFORM
LABEL \
    io.hass.name="ZingMusic" \
    io.hass.description="Music Assistant with ZingMusic Provider" \
    io.hass.version="${MASS_VERSION}" \
    io.hass.platform="${TARGETPLATFORM}" \
    io.hass.type="addon"

VOLUME [ "/data" ]
EXPOSE 8095

WORKDIR $VIRTUAL_ENV
ENTRYPOINT ["mass", "--config", "/data"]
