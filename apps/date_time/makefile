ROOT_DIR := $(shell pwd)
MODULE = "date_time"

# -------------------------------------------
# Testing
# -------------------------------------------
test:
	@echo "\033[0;34m[$(MODULE)] Running tests (pytest)...\033[0m"
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

clean-venv:
	@echo "\033[0;34m[$(MODULE)] Cleaning virtual environment(s)...\033[0m"
	@poetry env remove --all

clean: clean-venv clean-cache

install:
	@echo "\033[0;34m[$(MODULE)] Locking and installing dependencies...\033[0m"
	@poetry lock || exit 1 && poetry install || exit 1

# -------------------------------------------
# Server startup - dev only!
# -------------------------------------------
start:
	@echo "\033[0;31m[$(MODULE)] Starting development server (Ctrl + C to stop)...\033[0m"
	@poetry run uvicorn date_time.main:app --reload --host 0.0.0.0 --port 8000

# -------------------------------------------
# Help
# -------------------------------------------
help:
	@echo "\033[0;34mLocaleIQ [$(MODULE)] makefile commands:\033[0m"
	@echo "  clean       Clean virtual environments and caches"
	@echo "  clean-cache Clean pycache and pytest caches"
	@echo "  clean-venv  Clean venv environments"
	@echo "  format      Format code"
	@echo "  help        Show this help message"
	@echo "  install     Install [$(MODULE)] dependencies"
	@echo "  lint        Run all linting tasks (type-check, lint-fix, format)"
	@echo "  lint-fix    Run linting and auto-fix issues"
	@echo "  test        Run tests"
	@echo "  type-check  Run type checking"
