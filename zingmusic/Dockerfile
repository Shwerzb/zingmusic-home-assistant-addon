ARG BUILD_FROM
FROM ${BUILD_FROM}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install dependencies
RUN apk add --no-cache python3 py3-pip bash curl git jq

# Copy Music Assistant server source (only the actual server folder)
COPY music_assistant_server/music_assistant /app/music_assistant

# Copy your ZingMusic provider
COPY zingmusic_provider/ /app/music_assistant/providers/zingmusic/
COPY zingmusic_provider/__init__.py /app/music_assistant/providers/__init__.py

# Copy run script
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Start script
CMD [ "/run.sh" ]
