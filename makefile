# ===========================================
#  LocaleIQ Monorepo Makefile
# ===========================================

# List of all module directories (update as needed)
MODULES = apps/date_time packages/utils
ROOT_DIR := $(shell pwd)

# -------------------------------------------
# Testing
# -------------------------------------------
# Run tests for all modules async
test:
	@poetry run pytest -n auto --no-header

# Run tests for all modules synchronously
test-sync:
	@for m in $(MODULES); do \
        poetry run pytest --no-header $$m/tests & \
        wait; \
    done

# Run tests for a specific module: make test MODULE=apps/date_time
test-module:
	@if [ -z "$(MODULE)" ]; then \
        echo "Usage: make test-module MODULE=data"; \
    else \
        poetry run pytest --no-header ./$(MODULE); \
    fi
# -------------------------------------------
# Linting & Formatting
# -------------------------------------------
type-check:
	@for m in $(MODULES); do \
		poetry run mypy ./$$m || exit 1; \
		wait; \
    done

lint-fix:
	@for m in $(MODULES); do \
		poetry run ruff check --fix ./$$m || exit 1; \
		wait; \
	done

format:
	@for m in $(MODULES); do \
		poetry run ruff format ./$$m || exit 1; \
		wait; \
	done

lint: type-check lint-fix format
# -------------------------------------------
# Utility commands
# -------------------------------------------

clean-cache:
	@echo "Cleaning caches"
	@for module in $(MODULES); do \
		find $(ROOT_DIR)/$$module -type d -name "__pycache__" -exec rm -rf {} +; \
		find $(ROOT_DIR)/$$module -type d -name ".pytest_cache" -exec rm -rf {} +; \
	done

clean-venv:
	@echo "Cleaning virtual environments"
	@for module in $(MODULES); do \
		cd $(ROOT_DIR)/$$module && poetry env remove --all || true; \
	done

clean: clean-venv clean-cache
	@echo "Cleaned environments and caches."

# lock and install module dependencies
install:
	@for module in $(MODULES); do \
		cd $(ROOT_DIR)/$$module && poetry lock || exit 1 && poetry install || exit 1; \
	done

# list all modules of the monorepo
list:
	@for module in $(MODULES); do \
		echo " - $$module"; \
	done

# install git pre-commit hooks
prepare:
	poetry run pre-commit install
	wait

# setup a new environment or re-initialize an existing environment
setup: clean prepare install

# -------------------------------------------
# Help
# -------------------------------------------
help:
	@echo "🛠️ LocaleIQ Monorepo Makefile"
	@echo ""
	@echo "Available commands:"
	@echo "  clean       Clean virtual environments and caches"
	@echo "  clean-cache Clean pycache and pytest caches"
	@echo "  clean-env   Clean venv environments"
	@echo "  format      Format code in all modules"
	@echo "  help        Show this help message"
	@echo "  install     Install module dependencies"
	@echo "  lint        Run all linting tasks (type-check, lint-fix, format)"
	@echo "  lint-fix    Run linting and auto-fix issues on all modules"
	@echo "  list        List all modules in the monorepo"
	@echo "  test        Run tests for all modules asynchronously"
	@echo "  test-sync   Run tests for all modules serially"
	@echo "  type-check  Run type checking on all modules"
