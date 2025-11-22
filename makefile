# ===========================================
#  LocaleIQ Monorepo Makefile
# ===========================================

# List of all module directories (update as needed)
MODULES = shared data date_time language culture geopolitical economic

# -------------------------------------------
# Environment
# -------------------------------------------

# Install root dev environment (pytest, black, etc.)
install:
	poetry install

# Install dependencies for each module
install-modules:
	@for module in $(MODULES); do \
		echo "Installing $$module..."; \
		cd $$module && poetry install && cd ..; \
	done

# Full setup: root + all modules
setup: install install-modules
	@echo "Monorepo setup complete."

# -------------------------------------------
# Testing
# -------------------------------------------

# Run tests for all modules serial (root pytest.ini controls testpaths)
test:
	poetry run pytest -n auto

# Run tests for all modules in parallel (manual per-module invocation)
test-all:
	@echo "Running tests in parallel per module..."
	@for m in $(MODULES); do \
		echo "[TEST] $$m"; \
		poetry run pytest $$m/tests & \
	done; \
	wait
	@echo "Done."

# Run tests for a specific module: make test MODULE=data
test-module:
	@if [ -z "$(MODULE)" ]; then \
		echo "Usage: make test-module MODULE=data"; \
	else \
		poetry run pytest ./$(MODULE); \
	fi

# -------------------------------------------
# Linting & Formatting
# -------------------------------------------

format:
	poetry run black .
	poetry run isort .

lint:
	poetry run black --check .
	poetry run isort --check .
	poetry run mypy .

type-check:
	poetry run mypy .

# -------------------------------------------
# Utility
# -------------------------------------------

# Remove all poetry virtual environments
clean-venv:
	@echo "Removing venvs..."
	poetry env remove --all || true
	@for module in $(MODULES); do \
		echo "Removing venv for $$module..."; \
		cd $$module && poetry env remove --all || true; \
		cd ..; \
	done

# Remove all __pycache__
clean-pycache:
	@find . -type d -name "__pycache__" -exec rm -rf {} +

# Full clean
clean: clean-venv clean-pycache
	@echo "Clean complete."

# -------------------------------------------
# Help
# -------------------------------------------

help:
	@echo "LocaleIQ Monorepo Management"
	@echo ""
	@echo "Targets:"
	@echo "  setup             Install root + module dependencies"
	@echo "  install           Install root dependencies"
	@echo "  install-modules   Install dependencies for all modules"
	@echo "  test              Run full monorepo tests"
	@echo "  test-all          Run tests in all modules in parallel"
	@echo "  test-module       Run tests in one module (MODULE=name)"
	@echo "  format            Black + isort formatting"
	@echo "  lint              Black + isort + mypy checks"
	@echo "  type-check        Run mypy type checks"
	@echo "  clean             Remove venvs + caches"
	@echo "  clean-venv        Remove poetry virtualenvs"
	@echo "  clean-pycache     Remove __pycache__ folders"