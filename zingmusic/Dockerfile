ARG BUILD_FROM
FROM ${BUILD_FROM}

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install dependencies
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash \
    curl \
    jq

# Optional: install additional Python packages
# RUN pip3 install -r /requirements.txt

# Copy ZingMusic provider files
COPY zingmusic_provider/ /app/music_assistant/providers/zingmusic/
COPY zingmusic_provider/__init__.py /app/music_assistant/providers/__init__.py

# Copy entry script
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Set entrypoint
CMD [ "/run.sh" ]
