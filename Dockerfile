# syntax=docker/dockerfile:1.4

# Setup the builder image with Python and Poetry
FROM python:3.13-slim AS builder
WORKDIR /build
RUN pip install --upgrade pip && pip install poetry poetry-plugin-export
COPY pyproject.toml poetry.lock* ./
RUN poetry export -f requirements.txt --without-hashes --output requirements.txt

## Setup the runtime image
FROM python:3.13-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=2.1.3 \
    PYTHONPATH=/app/src
WORKDIR /app
COPY --from=builder /build/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd -m appuser
USER appuser

# Start the app with uvicorn
CMD ["python", "-m", "uvicorn", "localeiq.main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "2"]
