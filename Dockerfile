FROM public.ecr.aws/docker/library/python:3.12-slim

WORKDIR /app

# Install system dependencies for MySQL client
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements files
COPY pyproject.toml uv.lock* ./

# Install uv and dependencies
RUN pip install uv && \
    uv sync --frozen --no-dev

# Copy application code
COPY . .

# Copy and make startup script executable
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Expose port
EXPOSE 8000

# Run the startup script
CMD ["/app/start.sh"]
