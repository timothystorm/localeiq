# --- Builder stage ---
FROM python:3.14-alpine AS builder
WORKDIR /app

# Copy only what’s needed for build
COPY pyproject.toml README.md ./
COPY src ./src

# Install Poetry + build wheel
RUN pip install poetry && poetry build -f wheel

# --- Runtime stage ---
FROM python:3.14-alpine
WORKDIR /app

# Copy built wheel and install it
COPY --from=builder /app/dist/*.whl .
RUN pip install --no-cache-dir *.whl && rm *.whl

# Default command = Poetry script entry point
ENTRYPOINT ["python", "-m", "localeiq.server"]