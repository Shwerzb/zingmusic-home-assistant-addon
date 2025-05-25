ARG BUILD_FROM
FROM ${BUILD_FROM}

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install dependencies (if needed)
RUN apk add --no-cache bash curl jq

# Copy local files
COPY run.sh /run.sh

# Set permissions
RUN chmod a+x /run.sh

# Entrypoint
CMD [ "/run.sh" ]
