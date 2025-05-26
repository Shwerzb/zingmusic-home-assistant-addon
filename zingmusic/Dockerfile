FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install build dependencies
RUN pip install --no-cache-dir pip setuptools wheel

# Copy full source before install
COPY ./music_assistant /app/music_assistant
COPY ./zingmusic_provider /app/zingmusic_provider
COPY pyproject.toml ./  # must come after music_assistant is copied
COPY run.sh /app/run.sh

# Install the package (from the local source)
RUN pip install --no-cache-dir .

# Make run.sh executable
RUN chmod +x /app/run.sh

# Start the app
CMD ["/app/run.sh"]
