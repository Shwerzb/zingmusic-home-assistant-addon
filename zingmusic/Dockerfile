FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY pyproject.toml ./
RUN pip install --no-cache-dir .

# Copy your full app code
COPY ./music_assistant /app/music_assistant
COPY ./zingmusic_provider /app/zingmusic_provider
COPY run.sh /app/run.sh

# Make run.sh executable
RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
