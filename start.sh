#!/bin/bash
set -e

echo "Starting database..."
uv sync --frozen

echo "Running database migrations..."
uv run alembic upgrade head

echo "Running seed data..."
uv run seed.py

echo "Starting FastAPI application..."
exec uv run main.py
