FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file and install dependencies
COPY pyproject.toml ./
COPY requirements_all.txt ./

# Install Python dependencies (including Music Assistant Models, etc.)
RUN pip install --no-cache-dir -r requirements_all.txt

# Copy main application source
COPY ./music_assistant /app/music_assistant
COPY ./zingmusic_provider /app/zingmusic_provider

# Copy and make run script executable
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# Run the application
CMD ["/app/run.sh"]
