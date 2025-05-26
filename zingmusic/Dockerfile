# syntax=docker/dockerfile:1

ARG BASE_IMAGE_VERSION=latest
FROM ghcr.io/music-assistant/base:$BASE_IMAGE_VERSION AS builder

COPY requirements_all.txt .
COPY music_assistant /app/music_assistant
COPY zingmusic_provider /app/zingmusic_provider

# ensure UV is installed
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# create venv
ENV VIRTUAL_ENV=/app/venv
RUN uv venv $VIRTUAL_ENV

# install requirements
RUN uv pip install \
    --find-links "https://wheels.home-assistant.io/musllinux/" \
    -r requirements_all.txt

# install music assistant directly from source
RUN uv pip install /app/music_assistant

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
