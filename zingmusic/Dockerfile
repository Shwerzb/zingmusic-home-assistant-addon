ARG BUILD_FROM
FROM ${BUILD_FROM}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install dependencies
RUN apk add --no-cache python3 py3-pip bash curl jq

# Install Music Assistant server
RUN pip3 install music-assistant-server==2.5.2

# Copy custom ZingMusic provider
COPY zingmusic_provider/ /app/music_assistant/providers/zingmusic/
COPY zingmusic_provider/__init__.py /app/music_assistant/providers/__init__.py

# Entrypoint
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]
