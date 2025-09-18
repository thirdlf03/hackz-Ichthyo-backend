#!/bin/bash
set -e

echo "Starting database..."
# Set default host and port if not specified
MYSQL_HOST=${MYSQL_HOST}
MYSQL_PASSWORD=${MYSQL_PASSWORD}
MYSQL_PORT=${MYSQL_PORT:-3306}
MYSQL_USER=${MYSQL_USER}

# Wait for database to be ready
echo "Waiting for database connection..."
until uv run python -c "import pymysql; pymysql.connect(host='${MYSQL_HOST}', port=${MYSQL_PORT}, user='${MYSQL_USER}', password='${MYSQL_PASSWORD}', database='${MYSQL_DATABASE}')"; do
  echo "Database not ready, waiting..."
  sleep 2
done

echo "Running database migrations..."
uv run alembic upgrade head

echo "Running seed data..."
uv run seed.py

echo "Starting FastAPI application..."
exec uv run main.py
