#!/bin/bash
set -e

echo "Starting database..."

# Wait for database to be ready
echo "Waiting for database connection..."
until uv run python -c "import pymysql; pymysql.connect(host='${MYSQL_HOST}', port=int('${MYSQL_PORT}'), user='root', database='${MYSQL_DATABASE}')"; do
  echo "Database not ready, waiting..."
  sleep 2
done

echo "Running database migrations..."
uv run alembic upgrade head

echo "Running seed data..."
uv run seed.py

echo "Starting FastAPI application..."
exec uv run main.py
