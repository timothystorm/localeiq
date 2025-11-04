# --- Buuild ---
FROM python:3.14-slim AS builder
WORKDIR /app

# Copy only what’s needed for build
COPY pyproject.toml README.md ./
COPY src ./src

# Install Poetry + build wheel
RUN pip install poetry && poetry build -f wheel

# --- Runtime ---
FROM python:3.14-slim
WORKDIR /app

# Copy built wheel and install it
COPY --from=builder /app/dist/*.whl .
RUN pip install --no-cache-dir *.whl && rm *.whl

# Run the Uvicorn server
ENTRYPOINT ["python", "-m", "localeiq.server"]