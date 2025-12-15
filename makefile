# -----------------------------------------------------------------------------
# Make file for monorepo LocaleIQ project.
#
# Review the base makefile - ./.makefile_base
# ----------------------------------------------------------------------------

# Color codes
BLUE=\033[0;34m
CYAN=\033[0;36m
GREEN=\033[0;32m
NC=\033[0m # No Color
RED=\033[0;31m
YELLOW=\033[1;33m

help:
	@echo "✨ ${CYAN}COMMANDS:${NC}"
	@echo "  clean       Clean all build artifacts and virtual environments"
	@echo "  hooks       Install pre-commit git hooks"
	@echo "  lint        Run all linting tasks (type-check, lint-fix, format)"
	@echo "  pre-commit  Run pre-commit checks - useful before committing code"
	@echo "  setup       Lock and install dependencies"
	@echo "  test        Run tests synchronously"
	@echo "  venv        Setup and activate the Poetry virtual environment"
	@echo "  help        Show this help message"

clean:
	@echo "🧼  ${BLUE}CLEAN WORKSPACE...${NC}"
	@find packages apps -type d -name "__pycache__" -exec rm -rf {} +
	@find packages apps -type d -name ".mypy_cache" -exec rm -rf {} +
	@find packages apps -type d -name ".pytest_cache" -exec rm -rf {} +
	@find packages apps -type d -name ".ruff_cache" -exec rm -rf {} +

hooks:
	@echo "🔗  ${BLUE}INSTALL WORKSPACE PRE-COMMIT HOOKS...${NC}"
	@poetry run pre-commit install

lint:
	@echo "🎨  ${BLUE}LINT WORKSPACE...${NC}"
	@poetry run ruff format --quiet .
	@poetry run ruff check --fix --quiet .
	@poetry run mypy --no-error-summary packages apps

lint-check:
	@echo "🎨  ${BLUE}LINT WORKSPACE...${NC}"
	@poetry run ruff check --quiet .
	@poetry run mypy --no-error-summary packages apps

pre-commit:
	@echo "🔍  ${BLUE}RUN PRE-COMMIT CHECKS...${NC}"
	@poetry run pre-commit run --all-files

setup:
	@echo "🏗️  ${BLUE}SETUP WORKSPACE...${NC}"
	@poetry lock
	@poetry install
	@poetry run pre-commit install

test:
	@echo "🧪  ${BLUE}TEST WORKSPACE...${NC}"
	@poetry run pytest

venv:
	@echo "🐍 ${YELLOW}SETUP VIRTUAL ENVIRONMENT - RUN THIS COMMAND...${NC}"
	@poetry env activate
