ARG BUILD_FROM
FROM ${BUILD_FROM}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install required packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    git \
    bash \
    curl \
    jq

# Install Music Assistant server from GitHub (main branch)
RUN pip install git+https://github.com/music-assistant/server.git@main

# Copy custom ZingMusic provider into the container
COPY zingmusic_provider/ /app/music_assistant/providers/zingmusic/
COPY zingmusic_provider/__init__.py /app/music_assistant/providers/__init__.py

# Copy and configure the run script
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Start the Music Assistant server
CMD [ "/run.sh" ]
