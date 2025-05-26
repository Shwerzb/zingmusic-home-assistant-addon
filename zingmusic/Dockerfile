ARG BUILD_FROM
FROM ${BUILD_FROM}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install dependencies
RUN apk add --no-cache python3 py3-pip git curl bash jq

# Install Music Assistant server from GitHub
RUN pip install git+https://github.com/music-assistant/server.git@v2.5.2

# Copy ZingMusic provider
COPY zingmusic_provider/ /app/music_assistant/providers/zingmusic/
COPY zingmusic_provider/__init__.py /app/music_assistant/providers/__init__.py

# Entrypoint
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]
