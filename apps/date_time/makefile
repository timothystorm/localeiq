ROOT_DIR := $(shell pwd)
MODULE = "date_time"

# -------------------------------------------
# Testing
# -------------------------------------------
test:
	@echo "\033[0;34m[$(MODULE)] Running tests...\033[0m"
	@poetry run pytest -n auto --no-header

# -------------------------------------------
# Linting & Formatting
# -------------------------------------------
type-check:
	@echo "\033[0;34m[$(MODULE)] Type checking (mypy)...\033[0m"
	@poetry run mypy $(ROOT_DIR) || exit 1

lint-fix:
	@echo "\033[0;34m[$(MODULE)] Lint fix (ruff)...\033[0m"
	@poetry run ruff check --fix $(ROOT_DIR) || exit 1

format:
	@echo "\033[0;34m[$(MODULE)] Format (ruff)...\033[0m"
	@poetry run ruff format $(ROOT_DIR) || exit 1

lint: type-check lint-fix format

# -------------------------------------------
# Utility commands
# -------------------------------------------
clean-cache:
	@echo "\033[0;34m[$(MODULE)] Cleaning cache...\033[0m"
	@find $(ROOT_DIR) -type d -name "__pycache__" -exec rm -rf {} +
	@find $(ROOT_DIR) -type d -name ".pytest_cache" -exec rm -rf {} +

# -------------------------------------------
# Server startup - dev only!
# -------------------------------------------
start:
	@echo "\033[0;31m[$(MODULE)] Starting development server (Ctrl + C to stop)...\033[0m"
	@poetry run uvicorn date_time.main:app --reload --host 0.0.0.0 --port 8000