# LocaleIQ Development Task Runner (using just - https://github.com/casey/just)
# 
# This file contains ALL development commands.
# CI uses make (see makefile for CI-only commands).
#
# Install: brew install just (macOS) or cargo install just
# Usage: just <task>
# List all tasks: just --list

# Default recipe (runs when you type `just`)
default:
    @just --list

# -----------------------------------------------------------------------------
# Setup & Installation
# -----------------------------------------------------------------------------

# Initial project setup (run once) - installs everything you need
setup:
    @echo "🏗️  Setting up LocaleIQ workspace..."
    poetry lock
    poetry install
    poetry run pre-commit install
    @echo "✅ Setup complete! Run 'just dev' to start developing"

# Install dependencies only
install:
    @echo "📦 Installing dependencies..."
    poetry install

# Install pre-commit hooks
hooks:
    @echo "🔗 Installing pre-commit hooks..."
    poetry run pre-commit install

# Update dependencies
update:
    @echo "🔄 Updating dependencies..."
    poetry update

# Activate virtual environment (shows command to run)
venv:
    @echo "🐍 To activate the virtual environment, run:"
    @poetry env activate

# -----------------------------------------------------------------------------
# Development
# -----------------------------------------------------------------------------

# Start development server (REST API)
default_port := '8000'
dev port=default_port:
    @echo "🚀 Starting development server on port {{port}}..."
    @cd apps/rest_api && poetry run uvicorn rest_api.start:app --reload --reload-dir . --reload-dir {{justfile_directory()}}/packages --host 0.0.0.0 --port {{port}}

# Run CLI tool
cli *ARGS:
    @cd apps/cli_tool && poetry run python -m cli_tool.main {{ARGS}}

# -----------------------------------------------------------------------------
# Testing
# -----------------------------------------------------------------------------

# Run all tests
test:
    @echo "🧪 Running all tests..."
    poetry run pytest

# Run tests with coverage
test-cov:
    @echo "🧪 Running tests with coverage..."
    poetry run pytest --cov=apps --cov=packages --cov-report=term-missing --cov-report=html

# Run tests for specific module (e.g., just test-module apps/rest_api)
test-module module:
    @echo "🧪 Testing {{module}}..."
    cd {{module}} && poetry run pytest

# Run specific test file or pattern
test-match pattern:
    @echo "🧪 Running tests matching: {{pattern}}"
    poetry run pytest -k "{{pattern}}"

# Run tests in parallel (faster)
test-parallel:
    @echo "🧪 Running tests in parallel..."
    poetry run pytest -n auto

# Run tests and watch for changes (requires pytest-watch)
test-watch:
    @echo "👀 Running tests in watch mode..."
    @echo "Install pytest-watch: poetry add --group dev pytest-watch"
    poetry run ptw || echo "Run: poetry add --group dev pytest-watch"

# -----------------------------------------------------------------------------
# Linting & Formatting
# -----------------------------------------------------------------------------

# Run all linters and formatters
lint:
    @echo "🎨 Linting and formatting..."
    poetry run ruff format --quiet .
    poetry run ruff check --fix --quiet .
    poetry run mypy --no-error-summary packages apps

# Check linting without fixing
lint-check:
    @echo "🎨 Checking code quality..."
    poetry run ruff check --quiet .
    poetry run mypy --no-error-summary packages apps

# Format code only
format:
    @echo "🎨 Formatting code..."
    poetry run ruff format .

# Type check only
typecheck:
    @echo "🔍 Type checking..."
    poetry run mypy --no-error-summary packages apps

# Run pre-commit hooks manually
pre-commit:
    @echo "🔍 Running pre-commit checks..."
    poetry run pre-commit run --all-files

# -----------------------------------------------------------------------------
# Database
# -----------------------------------------------------------------------------

# Start database services
db-up:
    @echo "🐘 Starting database..."
    cd packages/data_store && docker compose -f docker-compose.local.yml up -d

# Stop database services
db-down:
    @echo "🐘 Stopping database..."
    cd packages/data_store && docker compose -f docker-compose.local.yml down

# View database logs
db-logs:
    @echo "📋 Database logs..."
    cd packages/data_store && docker compose -f docker-compose.local.yml logs -f

# Run database migrations
db-migrate:
    @echo "⬆️  Running migrations..."
    cd packages/data_store && poetry run alembic upgrade head

# Rollback last migration
db-rollback:
    @echo "⬇️  Rolling back migration..."
    cd packages/data_store && poetry run alembic downgrade -1

# Create new migration
db-new-migration message:
    @echo "📝 Creating migration: {{message}}"
    cd packages/data_store && poetry run alembic revision --autogenerate -m "{{message}}"

# Reset database (dangerous!)
db-reset:
    @echo "⚠️  Resetting database..."
    cd packages/data_store && poetry run alembic downgrade base
    cd packages/data_store && poetry run alembic upgrade head

# -----------------------------------------------------------------------------
# Cleanup
# -----------------------------------------------------------------------------

# Clean build artifacts and cache
clean:
    @echo "🧼 Cleaning workspace..."
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    @echo "✨ Clean!"

# Deep clean (includes venv)
clean-all: clean
    @echo "🧹 Deep cleaning (including venv)..."
    rm -rf .venv
    @echo "✨ Squeaky clean! Run 'just setup' to reinstall"

# -----------------------------------------------------------------------------
# Module-specific tasks
# -----------------------------------------------------------------------------

# Run task in specific module
run-in module task:
    @echo "🎯 Running '{{task}}' in {{module}}..."
    cd {{module}} && {{task}}

# Build CLI distribution
build-cli:
    @echo "📦 Building CLI tool..."
    cd apps/cli_tool && poetry build

# Build REST API distribution  
build-api:
    @echo "📦 Building REST API..."
    cd apps/rest_api && poetry build

# -----------------------------------------------------------------------------
# CI/CD helpers
# -----------------------------------------------------------------------------

# Run full CI suite locally
ci: lint test
    @echo "✅ CI checks passed!"

# Quick check before commit
quick: format test
    @echo "✅ Quick checks passed!"

# -----------------------------------------------------------------------------
# Documentation
# -----------------------------------------------------------------------------

# Generate API documentation
docs:
    @echo "📚 Generating documentation..."
    @echo "TODO: Add documentation generation"

# Serve documentation locally
docs-serve:
    @echo "📚 Serving documentation..."
    @echo "TODO: Add documentation server"

# -----------------------------------------------------------------------------
# Utilities
# -----------------------------------------------------------------------------

# Show project info
info:
    @echo "📊 LocaleIQ Project Info"
    @echo "========================"
    @echo "Python version: $(python --version)"
    @echo "Poetry version: $(poetry --version)"
    @echo ""
    @echo "Modules:"
    @echo "  - apps/rest_api (FastAPI)"
    @echo "  - apps/cli_tool (Typer)"
    @echo "  - packages/data_store (PostgreSQL + Alembic)"
    @echo "  - packages/utils (Config)"
    @echo ""
    @echo "Quick commands:"
    @echo "  just dev        - Start API server"
    @echo "  just test       - Run tests"
    @echo "  just lint       - Format and lint"
    @echo "  just db-up      - Start database"

# Check dependencies for security issues (requires safety)
security:
    @echo "🔒 Checking for security vulnerabilities..."
    @poetry run pip-audit || echo "Install pip-audit: poertry add --dev pip-audit"

# Show outdated dependencies
outdated:
    @echo "📦 Checking for outdated dependencies..."
    poetry show --outdated
