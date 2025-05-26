# syntax=docker/dockerfile:1

ARG BASE_IMAGE_VERSION=latest
FROM ghcr.io/music-assistant/base:$BASE_IMAGE_VERSION AS builder

COPY requirements_all.txt .
ADD dist dist

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Setup virtual environment
ENV VIRTUAL_ENV=/app/venv
RUN uv venv $VIRTUAL_ENV

# Install dependencies
RUN uv pip install \
    --find-links "https://wheels.home-assistant.io/musllinux/" \
    -r requirements_all.txt

# Install your custom music_assistant wheel
RUN uv pip install dist/music_assistant-*.whl

# Permissions
RUN chmod -R 777 /app

##################################################################################################

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
