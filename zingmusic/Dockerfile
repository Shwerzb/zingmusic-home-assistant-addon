FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install pip requirements
COPY pyproject.toml ./
COPY ./music_assistant ./music_assistant
COPY ./zingmusic_provider ./zingmusic_provider

# Install your local package (editable mode)
RUN pip install --no-cache-dir .

# Copy the startup script
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# Launch the server
CMD ["/app/run.sh"]
