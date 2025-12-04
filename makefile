# -----------------------------------------------------------------------------
# Make file for LocaleIQ Python modules.
#
# You can either include this base makefile in your module's makefile if you
# need to add custom commands, or use it directly as a symlink if you only.
#
# To include in a new module makefile, add (at the top of the module makefile):
# -include ../../.makefile
#
# To create a symlink in a new module directory, run:
# `ln -s ../../.makefile makefile`
#
# see: help target for enriching help output in child makefiles.
# ----------------------------------------------------------------------------
ROOT_DIR := $(shell pwd)
MODULE = $(notdir $(ROOT_DIR))

# ----------------------------------------------------------------------------
# Help
#
# Child makefiles can add `help-extra` target to add more help info.
# ----------------------------------------------------------------------------
help:
	@echo "\033[0;34m\033[0;34m[\033[0;33m$(MODULE)\033[0;34m] LocaleIQ makefile commands:\033[0m"
	@echo "  clean       Clean virtual environments and caches"
	@echo "  clean-cache Clean pycache and pytest caches"
	@echo "  clean-venv  Clean venv environments"
	@echo "  type-check  Run type checking"
	@echo "  lint-check  Run linting checks only"
	@echo "  lint-fix    Run linting and auto-fix issues"
	@echo "  format      Format code"
	@echo "  lint        Run all linting tasks (type-check, lint-fix, format)"
	@echo "  setup       Lock and install [$(MODULE)] dependencies"
	@echo "  test        Run tests synchronously"
	@echo "  test-async  Run tests asynchronously"
	@echo "  help        Show this help message"
	@$(MAKE) help-extra || true

# ----------------------------------------------------------------------------
# Testing
#
# Ensure pytest is installed in the module's poetry environment.
# ----------------------------------------------------------------------------
test:
	@echo "\033[0;34m[\033[0;33m$(MODULE)\033[0;34m] Running tests (pytest)...\033[0m"
	@poetry run pytest -v --tb=short --no-header

test-async:
	@echo "\033[0;34m[\033[0;33m$(MODULE)\033[0;34m] Running async tests (pytest-asyncio)...\033[0m"
	@poetry run pytest -v --tb=short --no-header -n auto

# ----------------------------------------------------------------------------
# Linting & Formatting
#
# Ensure mypy and ruff are installed in the module's poetry environment.
# ----------------------------------------------------------------------------
type-check:
	@echo "\033[0;34m[\033[0;33m$(MODULE)\033[0;34m] Type checking (mypy)...\033[0m"
	@poetry run mypy $(ROOT_DIR) || exit 1

lint-check:
	@echo "\033[0;34m[\033[0;33m$(MODULE)\033[0;34m] Lint check (ruff)...\033[0m"
	@poetry run ruff check $(ROOT_DIR) || exit 1

lint-fix:
	@echo "\033[0;34m[\033[0;33m$(MODULE)\033[0;34m] Lint fix (ruff)...\033[0m"
	@poetry run ruff check --fix $(ROOT_DIR) || exit 1

format:
	@echo "\033[0;34m[\033[0;33m$(MODULE)\033[0;34m] Format (ruff)...\033[0m"
	@poetry run ruff format $(ROOT_DIR) || exit 1

lint: type-check lint-fix format

# ----------------------------------------------------------------------------
# Utility commands
#
# Ensure poetry is installed on the system and poetry env is set up for the
# module.
# ----------------------------------------------------------------------------
clean-cache:
	@echo "\033[0;34m[\033[0;33m$(MODULE)\033[0;34m] Cleaning cache...\033[0m"
	@find $(ROOT_DIR) -type d -name "__pycache__" -exec rm -rf {} +
	@find $(ROOT_DIR) -type d -name ".mypy_cache" -exec rm -rf {} +
	@find $(ROOT_DIR) -type d -name ".pytest_cache" -exec rm -rf {} +
	@find $(ROOT_DIR) -type d -name ".ruff_cache" -exec rm -rf {} +

clean-venv:
	@echo "\033[0;34m[\033[0;33m$(MODULE)\033[0;34m] Cleaning virtual environment(s)...\033[0m"
	@poetry env remove --all

clean: clean-venv clean-cache

setup:
	@echo "\033[0;34m[\033[0;33m$(MODULE)\033[0;34m] Locking and installing dependencies...\033[0m"
	@poetry lock || exit 1 && poetry install || exit 1
