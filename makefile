# -----------------------------------------------------------------------------
# CI-Only Makefile for LocaleIQ
#
# This makefile contains ONLY commands used by CI/CD pipelines.
# For development tasks, use `just` (see justfile).
#
# Commands:
#   make setup       - Install dependencies (CI uses this)
#   make lint-check  - Check code quality without fixing (CI uses this)
#   make test        - Run test suite (CI uses this)
# ----------------------------------------------------------------------------

help:
	@echo "⚙️  CI-ONLY COMMANDS"
	@echo "  setup       Install dependencies (CI)"
	@echo "  lint-check  Check code quality (CI)"
	@echo "  test        Run tests (CI)"
	@echo ""
	@echo "💡 For development commands, use: just --list"
	@echo "   Install just: brew install just"

setup:
	@echo "🏗️  Installing dependencies for CI..."
	@poetry install

lint-check:
	@echo "🎨  Checking code quality (CI)..."
	@poetry run ruff check --quiet .
	@poetry run mypy --no-error-summary packages apps

test:
	@echo "🧪  Running tests (CI)..."
	@poetry run pytest
