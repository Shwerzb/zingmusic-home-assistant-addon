# syntax=docker/dockerfile:1

ARG BASE_IMAGE_VERSION=latest
FROM ghcr.io/music-assistant/base:$BASE_IMAGE_VERSION AS builder

WORKDIR /app

# Add dist folder that contains the built wheel
ADD dist dist

# Install UV (ultra-fast pip)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create venv for runtime
ENV VIRTUAL_ENV=/app/venv
RUN uv venv $VIRTUAL_ENV

# Install your wheel package from dist
RUN uv pip install \
    --find-links "https://wheels.home-assistant.io/musllinux/" \
    dist/music_assistant-*.whl

# Set full permissions so HA Supervisor can access everything
RUN chmod -R 777 /app

##################################################################################################

FROM ghcr.io/music-assistant/base:$BASE_IMAGE_VERSION

ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy installed venv and runtime files
COPY --from=builder /app /app

RUN chmod 777 /app

LABEL \
    io.hass.name="ZingMusic" \
    io.hass.description="ZingMusic Add-on for Music Assistant" \
    io.hass.version="1.0.0" \
    io.hass.type="addon"

VOLUME [ "/data" ]
EXPOSE 8095

WORKDIR /app

CMD [ "/app/run.sh" ]
