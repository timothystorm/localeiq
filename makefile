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
	@echo "  lint        Run all linting tasks (type-check, lint-fix, format)"
	@echo "  setup       Lock and install dependencies"
	@echo "  test        Run tests synchronously"
	@echo "  help        Show this help message"

clean:
	@echo "🧼  ${BLUE}CLEAN WORKSPACE...${NC}"
	@find packages apps -type d -name "__pycache__" -exec rm -rf {} +
	@find packages apps -type d -name ".mypy_cache" -exec rm -rf {} +
	@find packages apps -type d -name ".pytest_cache" -exec rm -rf {} +
	@find packages apps -type d -name ".ruff_cache" -exec rm -rf {} +

lint:
	@echo "🎨  ${BLUE}LINT WORKSPACE...${NC}"
	@poetry run ruff format --quiet .
	@poetry run ruff check --fix --quiet .
	@poetry run mypy --no-error-summary packages apps

setup:
	@echo "🏗️  ${BLUE}SETUP WORKSPACE...${NC}"
	@poetry lock
	@poetry install
	@poetry env use $$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')") >/dev/null 2>&1
	@poetry run pre-commit install

test:
	@echo "🧪  ${BLUE}TEST WORKSPACE...${NC}"
	@poetry run pytest
